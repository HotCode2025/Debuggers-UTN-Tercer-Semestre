from datetime import datetime, timedelta

from .models import Disponibilidad, Turno

def obtener_horarios_disponibles(profesional,establecimiento,especialidad,fecha):
    dia_semana = fecha.weekday()

    disponibilidades = Disponibilidad.objects.filter(
        profesional = profesional,
        establecimiento =establecimiento,
        especialidad =especialidad,
        dia_semana=dia_semana,
    )

    horarios_disponibles = []

    for disponibilidad in disponibilidades:
        inicio = datetime.combine(fecha, disponibilidad.hora_inicio)
        fin = datetime.combine(fecha, disponibilidad.hora_fin)
        duracion = timedelta(minutes=disponibilidad.duracion_turno_minutos)

        horario_actual = inicio

        while horario_actual + duracion <= fin:
            hora = horario_actual.time()

            turno_ocupado= Turno.objects.filter(
                profesional=profesional,
                fecha = fecha,
                hora = hora,
                estado= Turno.RESERVADO,
            ).exists()

            if not turno_ocupado:
                horarios_disponibles.append(hora)

            horario_actual += duracion

    return horarios_disponibles

def reservar_turno(usuario, profesional, establecimiento, especialidad, fecha, hora):
   if fecha.weekday() > 4:
       raise ValueError("No se pueden reservar turnos para fines de semana")
   
   horarios_disponibles = obtener_horarios_disponibles(
       profesional=profesional,
       establecimiento=establecimiento,
       especialidad=especialidad,
       fecha=fecha,
    )
   
   if hora not in horarios_disponibles:
         raise ValueError("El horario seleccionado no está disponible")
   
   turno = Turno.objects.create(
       usuario=usuario,
       profesional=profesional,
       establecimiento=establecimiento,
       especialidad=especialidad,
       fecha=fecha,
       hora=hora,
       estado=Turno.RESERVADO
   )

   return turno