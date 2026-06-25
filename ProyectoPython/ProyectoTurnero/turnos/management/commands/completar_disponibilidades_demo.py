"""Garantiza horarios de consultorio para todas las relaciones médicas demo."""

from datetime import time

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from turnos.models import (
    Disponibilidad,
    ProfesionalEstablecimientoEspecialidad,
)


class Command(BaseCommand):
    help = (
        "Crea disponibilidades de lunes a viernes para cada médico, "
        "establecimiento y especialidad habilitados."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--hora-inicio",
            default="08:00",
            help="Hora inicial en formato HH:MM. Valor predeterminado: 08:00.",
        )
        parser.add_argument(
            "--hora-fin",
            default="12:00",
            help="Hora final en formato HH:MM. Valor predeterminado: 12:00.",
        )
        parser.add_argument(
            "--duracion",
            type=int,
            default=30,
            help="Duración de cada turno en minutos. Valor predeterminado: 30.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        hora_inicio = self._convertir_hora(options["hora_inicio"])
        hora_fin = self._convertir_hora(options["hora_fin"])
        duracion = options["duracion"]

        if hora_inicio >= hora_fin:
            self.stderr.write(
                self.style.ERROR(
                    "La hora de inicio debe ser menor que la hora de fin."
                )
            )
            return

        if duracion <= 0:
            self.stderr.write(
                self.style.ERROR("La duración debe ser mayor que cero.")
            )
            return

        relaciones = (
            ProfesionalEstablecimientoEspecialidad.objects
            .select_related("profesional", "establecimiento", "especialidad")
            .all()
        )

        creadas = 0
        existentes = 0

        for relacion in relaciones:
            # Los valores 0 a 4 coinciden con lunes a viernes en el modelo.
            for dia_semana in range(5):
                ya_existe = Disponibilidad.objects.filter(
                    profesional=relacion.profesional,
                    establecimiento=relacion.establecimiento,
                    especialidad=relacion.especialidad,
                    dia_semana=dia_semana,
                ).exists()

                if ya_existe:
                    existentes += 1
                    continue

                Disponibilidad.objects.create(
                    profesional=relacion.profesional,
                    establecimiento=relacion.establecimiento,
                    especialidad=relacion.especialidad,
                    dia_semana=dia_semana,
                    hora_inicio=hora_inicio,
                    hora_fin=hora_fin,
                    duracion_turno_minutos=duracion,
                )
                creadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                "Disponibilidades de consultorio completadas correctamente."
            )
        )
        self.stdout.write(f"Relaciones médicas procesadas: {relaciones.count()}")
        self.stdout.write(f"Disponibilidades nuevas: {creadas}")
        self.stdout.write(f"Disponibilidades que ya existían: {existentes}")
        self.stdout.write(
            f"Horario aplicado: lunes a viernes, "
            f"{hora_inicio.strftime('%H:%M')} a {hora_fin.strftime('%H:%M')}, "
            f"turnos de {duracion} minutos."
        )

    def _convertir_hora(self, valor):
        """Convierte HH:MM en time y muestra un error claro si es inválido."""
        try:
            horas, minutos = (int(parte) for parte in valor.split(":"))
            return time(horas, minutos)
        except (TypeError, ValueError):
            raise CommandError(
                f"La hora '{valor}' no tiene el formato HH:MM."
            )
