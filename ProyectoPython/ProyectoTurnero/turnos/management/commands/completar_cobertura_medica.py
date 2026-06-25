"""Completa la cobertura demo de médicos para cada centro y especialidad."""

from datetime import time

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

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


NOMBRES = [
    "Agustín", "Ana", "Camila", "Carla", "Diego", "Elena",
    "Federico", "Florencia", "Gabriel", "Joaquín", "Laura", "Lucía",
]

APELLIDOS = [
    "Acosta", "Benítez", "Castro", "Díaz", "Fernández", "García",
    "Gómez", "López", "Martínez", "Medina", "Molina", "Navarro",
]

PASSWORD_DEMO = "TurneroDemo2026!"


class Command(BaseCommand):
    help = (
        "Garantiza tres médicos para cada combinación de provincia, "
        "establecimiento y especialidad."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--cantidad",
            type=int,
            choices=range(3, 6),
            default=3,
            help="Médicos por especialidad y provincia (entre 3 y 5).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        cantidad = options["cantidad"]
        especialidades = list(Especialidad.objects.all().order_by("id"))
        provincias = list(
            Ciudad.objects.values_list("provincia", flat=True)
            .distinct()
            .order_by("provincia")
        )

        if not especialidades:
            self.stderr.write(
                self.style.ERROR(
                    "No hay especialidades. Ejecutá primero cargar_datos_demo."
                )
            )
            return

        asociaciones_creadas = 0
        profesionales_preparados = 0

        for provincia_indice, provincia in enumerate(provincias):
            establecimientos = list(
                Establecimiento.objects.filter(
                    ciudad__provincia=provincia
                ).order_by("id")
            )

            if not establecimientos:
                continue

            for especialidad_indice, especialidad in enumerate(especialidades):
                # Todos los centros de la provincia publican la especialidad.
                for establecimiento in establecimientos:
                    EstablecimientoEspecialidad.objects.get_or_create(
                        establecimiento=establecimiento,
                        especialidad=especialidad,
                    )

                # El grupo médico se comparte entre los establecimientos de la
                # provincia y mantiene una especialidad profesional coherente.
                for numero in range(1, cantidad + 1):
                    profesional = self._obtener_profesional(
                        provincia=provincia,
                        provincia_indice=provincia_indice,
                        especialidad=especialidad,
                        especialidad_indice=especialidad_indice,
                        numero=numero,
                    )
                    profesionales_preparados += 1

                    for centro_indice, establecimiento in enumerate(establecimientos):
                        _, creada = (
                            ProfesionalEstablecimientoEspecialidad.objects.get_or_create(
                                profesional=profesional,
                                establecimiento=establecimiento,
                                especialidad=especialidad,
                            )
                        )
                        asociaciones_creadas += int(creada)

                        # Una franja semanal permite que la búsqueda de horarios
                        # también funcione para las relaciones recién agregadas.
                        dia = (
                            provincia_indice
                            + especialidad_indice
                            + numero
                            + centro_indice
                        ) % 5
                        Disponibilidad.objects.get_or_create(
                            profesional=profesional,
                            establecimiento=establecimiento,
                            especialidad=especialidad,
                            dia_semana=dia,
                            hora_inicio=time(8, 0),
                            hora_fin=time(12, 0),
                            defaults={"duracion_turno_minutos": 30},
                        )

        self.stdout.write(
            self.style.SUCCESS("Cobertura médica demo completada.")
        )
        self.stdout.write(
            f"Grupos médico/provincia/especialidad preparados: "
            f"{profesionales_preparados}"
        )
        self.stdout.write(
            f"Nuevas asociaciones con establecimientos: {asociaciones_creadas}"
        )
        self.stdout.write(
            self.style.WARNING(
                f"Contraseña de las cuentas nuevas: {PASSWORD_DEMO}"
            )
        )

    def _obtener_profesional(
        self,
        provincia,
        provincia_indice,
        especialidad,
        especialidad_indice,
        numero,
    ):
        """Crea o recupera un médico estable para provincia y especialidad."""
        provincia_slug = slugify(provincia)[:18]
        especialidad_slug = slugify(especialidad.nombre)[:18]
        username = (
            f"doc_{provincia_slug}_{especialidad_slug}_{numero}"
        )[:150]
        matricula = (
            f"DEMO-{provincia_indice + 1:02d}-"
            f"{especialidad_indice + 1:02d}-{numero:02d}"
        )

        nombre = NOMBRES[
            (provincia_indice + especialidad_indice + numero) % len(NOMBRES)
        ]
        apellido = APELLIDOS[
            (provincia_indice * 2 + especialidad_indice + numero) % len(APELLIDOS)
        ]

        usuario, creado = User.objects.get_or_create(
            username=username,
            defaults={
                "first_name": nombre,
                "last_name": apellido,
                "email": f"{username}@turnero.local",
            },
        )
        if creado:
            usuario.set_password(PASSWORD_DEMO)
            usuario.save(update_fields=["password"])

        PerfilUsuario.objects.update_or_create(
            usuario=usuario,
            defaults={"rol": PerfilUsuario.MEDICO},
        )
        # La relación con User es uno-a-uno. Si una ejecución anterior ya creó
        # el profesional con otra matrícula, se reutiliza esa misma fila.
        profesional = Profesional.objects.filter(usuario=usuario).first()

        if profesional is None:
            profesional = Profesional.objects.filter(matricula=matricula).first()

        if profesional is None:
            profesional = Profesional.objects.create(
                usuario=usuario,
                matricula=matricula,
                nombre=nombre,
                apellido=apellido,
            )
        else:
            profesional.usuario = usuario
            profesional.nombre = nombre
            profesional.apellido = apellido
            profesional.save(update_fields=["usuario", "nombre", "apellido"])

        return profesional
