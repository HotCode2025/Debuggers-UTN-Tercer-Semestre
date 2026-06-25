"""Genera datos reproducibles para probar el turnero."""

import random
from datetime import time

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from turnos.models import (
    Ciudad,
    Disponibilidad,
    Especialidad,
    Establecimiento,
    EstablecimientoEspecialidad,
    PerfilUsuario,
    Profesional,
    ProfesionalEstablecimientoEspecialidad,
)


JURISDICCIONES = [
    ("Buenos Aires", "La Plata"),
    ("CABA", "Ciudad Autónoma de Buenos Aires"),
    ("Catamarca", "San Fernando del Valle de Catamarca"),
    ("Chaco", "Resistencia"),
    ("Chubut", "Rawson"),
    ("Córdoba", "Córdoba"),
    ("Corrientes", "Corrientes"),
    ("Entre Ríos", "Paraná"),
    ("Formosa", "Formosa"),
    ("Jujuy", "San Salvador de Jujuy"),
    ("La Pampa", "Santa Rosa"),
    ("La Rioja", "La Rioja"),
    ("Mendoza", "Mendoza"),
    ("Misiones", "Posadas"),
    ("Neuquén", "Neuquén"),
    ("Río Negro", "Viedma"),
    ("Salta", "Salta"),
    ("San Juan", "San Juan"),
    ("San Luis", "San Luis"),
    ("Santa Cruz", "Río Gallegos"),
    ("Santa Fe", "Santa Fe"),
    ("Santiago del Estero", "Santiago del Estero"),
    ("Tierra del Fuego", "Ushuaia"),
    ("Tucumán", "San Miguel de Tucumán"),
]

ESPECIALIDADES = [
    "Cardiología", "Clínica Médica", "Dermatología", "Endocrinología",
    "Gastroenterología", "Ginecología", "Neurología", "Oftalmología",
    "Pediatría", "Traumatología", "Urología", "Otorrinolaringología",
]

NOMBRES = [
    "Agustín", "Ana", "Camila", "Carla", "Diego", "Elena", "Federico",
    "Florencia", "Gabriel", "Joaquín", "Laura", "Lucía", "Marcos",
    "Martina", "Natalia", "Nicolás", "Paula", "Santiago", "Sofía", "Tomás",
]

APELLIDOS = [
    "Acosta", "Benítez", "Castro", "Díaz", "Fernández", "García", "Gómez",
    "López", "Martínez", "Medina", "Molina", "Navarro", "Pereyra", "Pérez",
    "Ramírez", "Romero", "Ruiz", "Sánchez", "Silva", "Torres",
]

CALLES = [
    "9 de Julio", "Alberdi", "Belgrano", "Brown", "Colón", "España",
    "General Paz", "Independencia", "Las Heras", "Libertad", "Mitre",
    "Moreno", "Rivadavia", "San Martín", "Sarmiento", "Urquiza",
]

TIPOS_CENTRO = [
    "Centro Médico", "Clínica", "Hospital", "Instituto Médico",
    "Policonsultorio", "Sanatorio",
]

REFERENCIAS_CENTRO = [
    "del Centro", "del Parque", "del Sol", "Federal", "Integral",
    "Los Andes", "Norte", "San Gabriel", "San José", "Santa María",
]

PASSWORD_DEMO = "TurneroDemo2026!"


class Command(BaseCommand):
    help = (
        "Carga 20 establecimientos por jurisdicción, 20 pacientes, "
        "20 médicos y sus relaciones de atención."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--semilla",
            type=int,
            default=2026,
            help="Permite reproducir la misma selección aleatoria.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        random.seed(options["semilla"])

        especialidades = self._crear_especialidades()
        establecimientos = self._crear_establecimientos(especialidades)
        pacientes = self._crear_pacientes()
        profesionales = self._crear_medicos(establecimientos, especialidades)

        self.stdout.write(self.style.SUCCESS("Datos de demostración preparados."))
        self.stdout.write(f"Jurisdicciones: {len(JURISDICCIONES)}")
        self.stdout.write(f"Establecimientos demo: {len(establecimientos)}")
        self.stdout.write(f"Pacientes demo: {len(pacientes)}")
        self.stdout.write(f"Médicos demo: {len(profesionales)}")
        self.stdout.write(
            self.style.WARNING(
                f"Contraseña compartida de las cuentas demo: {PASSWORD_DEMO}"
            )
        )

    def _crear_especialidades(self):
        """Crea el catálogo médico compartido por centros y profesionales."""
        return [
            Especialidad.objects.get_or_create(nombre=nombre)[0]
            for nombre in ESPECIALIDADES
        ]

    def _crear_establecimientos(self, especialidades):
        """Crea una capital y veinte establecimientos por jurisdicción."""
        resultado = []

        for provincia, capital in JURISDICCIONES:
            ciudad, _ = Ciudad.objects.get_or_create(
                nombre=capital,
                provincia=provincia,
            )

            for numero in range(1, 21):
                tipo_nombre = TIPOS_CENTRO[(numero - 1) % len(TIPOS_CENTRO)]
                referencia = REFERENCIAS_CENTRO[(numero - 1) % len(REFERENCIAS_CENTRO)]
                nombre = f"{tipo_nombre} Demo {referencia} {numero:02d} - {provincia}"
                tipo = (
                    Establecimiento.PUBLICO
                    if numero % 3 == 0
                    else Establecimiento.PRIVADO
                )

                establecimiento, _ = Establecimiento.objects.get_or_create(
                    nombre=nombre,
                    ciudad=ciudad,
                    defaults={
                        "tipo": tipo,
                        "direccion": f"{random.choice(CALLES)} {random.randint(100, 4999)}",
                    },
                )

                for especialidad in random.sample(especialidades, k=5):
                    EstablecimientoEspecialidad.objects.get_or_create(
                        establecimiento=establecimiento,
                        especialidad=especialidad,
                    )

                resultado.append(establecimiento)

        return resultado

    def _crear_pacientes(self):
        """Crea pacientes que ingresan usando el DNI generado como username."""
        pacientes = []

        for indice in range(1, 21):
            nombre = NOMBRES[(indice - 1) % len(NOMBRES)]
            apellido = APELLIDOS[(indice + 3) % len(APELLIDOS)]
            documento = str(47000000 + indice)
            provincia, ciudad = JURISDICCIONES[(indice - 1) % len(JURISDICCIONES)]

            usuario, creado = User.objects.get_or_create(
                username=documento,
                defaults={
                    "first_name": nombre,
                    "last_name": apellido,
                    "email": f"paciente.demo{indice:02d}@turnero.local",
                },
            )
            if creado:
                usuario.set_password(PASSWORD_DEMO)
                usuario.save(update_fields=["password"])

            PerfilUsuario.objects.update_or_create(
                usuario=usuario,
                defaults={
                    "rol": PerfilUsuario.PACIENTE,
                    "tipo_documento": "DNI",
                    "documento": documento,
                    "genero": "Prefiero no decirlo",
                    "provincia": provincia,
                    "ciudad": ciudad,
                    "telefono": f"11-5555-{indice:04d}",
                },
            )
            pacientes.append(usuario)

        return pacientes

    def _crear_medicos(self, establecimientos, especialidades):
        """Crea médicos con dos sedes y horarios semanales utilizables."""
        profesionales = []

        for indice in range(1, 21):
            nombre = NOMBRES[(indice + 5) % len(NOMBRES)]
            apellido = APELLIDOS[(indice + 9) % len(APELLIDOS)]
            username = f"medico_demo_{indice:02d}"
            matricula = f"DEMO-MP-{indice:05d}"

            usuario, creado = User.objects.get_or_create(
                username=username,
                defaults={
                    "first_name": nombre,
                    "last_name": apellido,
                    "email": f"medico.demo{indice:02d}@turnero.local",
                },
            )
            if creado:
                usuario.set_password(PASSWORD_DEMO)
                usuario.save(update_fields=["password"])

            PerfilUsuario.objects.update_or_create(
                usuario=usuario,
                defaults={"rol": PerfilUsuario.MEDICO},
            )
            profesional, _ = Profesional.objects.update_or_create(
                matricula=matricula,
                defaults={
                    "usuario": usuario,
                    "nombre": nombre,
                    "apellido": apellido,
                },
            )

            provincia_indice = (indice - 1) % len(JURISDICCIONES)
            inicio = provincia_indice * 20
            sedes = random.sample(establecimientos[inicio:inicio + 20], k=2)

            ids_1 = set(
                EstablecimientoEspecialidad.objects.filter(
                    establecimiento=sedes[0]
                ).values_list("especialidad_id", flat=True)
            )
            ids_2 = set(
                EstablecimientoEspecialidad.objects.filter(
                    establecimiento=sedes[1]
                ).values_list("especialidad_id", flat=True)
            )
            comunes = list(ids_1 & ids_2)

            if comunes:
                especialidad = Especialidad.objects.get(id=random.choice(comunes))
            else:
                especialidad = random.choice(especialidades)
                for sede in sedes:
                    EstablecimientoEspecialidad.objects.get_or_create(
                        establecimiento=sede,
                        especialidad=especialidad,
                    )

            for sede in sedes:
                ProfesionalEstablecimientoEspecialidad.objects.get_or_create(
                    profesional=profesional,
                    establecimiento=sede,
                    especialidad=especialidad,
                )

                for dia in ((indice - 1) % 5, (indice + 1) % 5):
                    Disponibilidad.objects.get_or_create(
                        profesional=profesional,
                        establecimiento=sede,
                        especialidad=especialidad,
                        dia_semana=dia,
                        hora_inicio=time(8, 0),
                        hora_fin=time(12, 0),
                        defaults={"duracion_turno_minutos": 30},
                    )

            profesionales.append(profesional)

        return profesionales
