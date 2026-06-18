from datetime import date, datetime, timedelta

from .models import (
    Disponibilidad,
    Especialidad,
    Profesional, 
    Turno,
    ProfesionalEstablecimientoEspecialidad,
    Establecimiento,
    EstablecimientoEspecialidad,
)

def obtener_horarios_disponibles(profesional,establecimiento,especialidad,fecha):
    dia_semana = fecha.weekday()

    if dia_semana > 4:
        return []

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
   if fecha < date.today():
       raise ValueError("No se pueden reservar turnos para fechas pasadas")
   
   if fecha.weekday() > 4:
         raise ValueError("No se pueden reservar turnos para fines de semana")
   
   profesional_habilitado = ProfesionalEstablecimientoEspecialidad.objects.filter(
       profesional=profesional,
       establecimiento=establecimiento,
       especialidad=especialidad
   ).exists()

   if not profesional_habilitado:
            raise ValueError("El profesional no está habilitado para esta especialidad en este establecimiento")    
   
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

def obtener_establecimientos_por_ciudad(ciudad):
     return Establecimiento.objects.filter(ciudad=ciudad)

def obtener_especialidades_por_establecimiento(establecimiento):
     especialidades_ids =EstablecimientoEspecialidad.objects.filter(
          establecimiento=establecimiento
     ).values_list("especialidad_id", flat=True)

     return Especialidad.objects.filter(id__in=especialidades_ids)

def obtener_profesionales_por_establecimiento_y_especialidad(
          establecimiento,
          especialidad
):
     profesionales_ids = ProfesionalEstablecimientoEspecialidad.objects.filter(
          establecimiento=establecimiento,
          especialidad=especialidad,
     ).values_list("profesional_id", flat=True)

     return Profesional.objects.filter(id__in=profesionales_ids)

def obtener_turnos_de_usuario(usuario):
     return Turno.objects.filter(
          usuario=usuario,
          ).order_by("fecha", "hora")

def obtener_turnos_activos_de_usuario(usuario):
     return Turno.objects.filter (
          usuario = usuario,
          estado= Turno.RESERVADO,
     ).order_by("fecha","hora")


def cancelar_turno(usuario, turno):
     if turno.usuario != usuario:
          raise ValueError("No podes cancelar un turno que pertenece a otro usuario.")
     
     if turno.estado != Turno.RESERVADO:
          raise ValueError("Solo se pueden cancelar turnos reservados.")
     
     turno.estado = Turno.CANCELADO
     turno.save()

     return turno

def obtener_profesional_de_usuario(usuario):
     try: 
          return usuario.perfil_profesional
     except Profesional.DoesNotExist:
          raise ValueError("El usuario no tiene un perfil profesional asociado.")
     
def obtener_turnos_de_profesional(profesional):
     return Turno.objects.filter(
          profesional=profesional,
     ).order_by("fecha","hora")

def obtener_turnos_activos_de_profesional(profesional):
     return Turno.objects.filter(
          profesional=profesional,
          estado=Turno.RESERVADO,
     ).order_by("fecha","hora")

def obtener_turnos_de_profesional_por_fecha(profesional,fecha):
     return Turno.objects.filter(
          profesional=profesional,
          fecha=fecha,
          estado=Turno.RESERVADO,
     ).order_by("hora")

def obtener_disponibilidades_de_profesional(profesional):
     return Disponibilidad.objects.filter(
          profesional = profesional,
     ).order_by("dia_semana","hora_inicio")

def existe_disponibilidad_superpuesta(
          profesional,
          establecimiento,
          especialidad,
          dia_semana,
          hora_inicio,
          hora_fin,
          disponibilidad_excluida=None,
):
     disponibilidades = Disponibilidad.objects.filter(
          profesional=profesional,
          establecimiento=establecimiento,
          especialidad=especialidad,
          dia_semana=dia_semana,
     )

     if disponibilidad_excluida:
          disponibilidades = disponibilidades.exclude(id=disponibilidad_excluida.id)

     return disponibilidades.filter(
          hora_inicio__lt=hora_fin,
          hora_fin__gt=hora_inicio,
     ).exists()

def crear_disponibilidad_profesional(
          profesional,
          establecimiento,
          especialidad,
          dia_semana,
          hora_inicio,
          hora_fin,
          duracion_turno_minutos,
):
    if dia_semana < 0 or dia_semana > 4:
          raise ValueError("El dia de atención debe ser de lunes a viernes.")
    
    if hora_inicio >= hora_fin:
         raise ValueError ("La hora de inicio debe ser menor que la hora de fin")
    
    profesional_habilitado = ProfesionalEstablecimientoEspecialidad.objects.filter(
         profesional = profesional,
         establecimiento=establecimiento,
         especialidad=especialidad,
    ).exists()

    if not profesional_habilitado:
         raise ValueError(
              "El profesional no atiende esa especialidad en ese establecimiento."
         )
    
    if existe_disponibilidad_superpuesta(
         profesional=profesional,
         establecimiento=establecimiento,
         especialidad=especialidad,
         dia_semana=dia_semana,
         hora_inicio=hora_inicio,
         hora_fin=hora_fin,
    ):
         raise ValueError("Ya existe una disponibilidad superpuesta para ese dia y horario.")

    disponibilidad = Disponibilidad.objects.create(
         profesional=profesional,
         establecimiento=establecimiento,
         especialidad=especialidad,
         dia_semana=dia_semana,
         hora_inicio=hora_inicio,
         hora_fin= hora_fin,
         duracion_turno_minutos=duracion_turno_minutos,
    )

    return disponibilidad

def modificar_disponibilidad_profesional(
          disponibilidad,
          profesional,
          establecimiento,
          especialidad,
          dia_semana,
          hora_inicio,
          hora_fin,
          duracion_turno_minutos,
): 
    if disponibilidad.profesional != profesional:
         raise ValueError("No podes modificar una disponibilidad de otro profesional.")
    if dia_semana < 0 or dia_semana > 4:
         raise ValueError("El día de atencion debe ser de Lunes a Viernes.")
    if hora_inicio >= hora_fin:
         raise ValueError("La hora de inicio debe ser menor que la hora de fin.") 
    
    profesional_habilitado = ProfesionalEstablecimientoEspecialidad.objects.filter(
         profesional=profesional,
         establecimiento=establecimiento,
         especialidad=especialidad,
    ).exists()

    if not profesional_habilitado:
         raise ValueError(
              "El profesional no atiende esa especialidad en ese establecimiento."
         )
    
    if existe_disponibilidad_superpuesta(
         profesional=profesional,
         establecimiento=establecimiento,
         especialidad=especialidad,
         dia_semana=dia_semana,
         hora_inicio=hora_inicio,
         hora_fin=hora_fin,
         disponibilidad_excluida=disponibilidad,
    ):
         raise ValueError("Ya existe una disponibilidad superpuesta para ese día y horario.")
    
    
    disponibilidad.establecimiento = establecimiento
    disponibilidad.especialidad = especialidad
    disponibilidad.dia_semana=dia_semana
    disponibilidad.hora_inicio=hora_inicio
    disponibilidad.hora_fin=hora_fin
    disponibilidad.duracion_turno_minutos=duracion_turno_minutos
    disponibilidad.save()

    return disponibilidad

def eliminar_disponibilidad_profesional(disponibilidad, profesional):
    if disponibilidad.profesional != profesional:
         raise ValueError("No Podes eliminar una disponibilidad de otro profesional")
    
    disponibilidad.delete()

def marcar_turno_como_atendido(turno,profesional):
     if turno.profesional != profesional:
          raise ValueError("No podes modificar un turno de otro profesional.")
     
     if turno.estado != Turno.RESERVADO:
          raise ValueError("Solo un turno reservado puede marcarse como atendido.")
     
     turno.estado = Turno.ATENDIDO
     turno.save(update_fields=["estado"])

     return turno

def cancelar_turno_como_profesional(turno,profesional):
     if turno.profesional != profesional:
          raise ValueError("No podes cancelar un turno de otro profesional.")
     
     if turno.estado != Turno.RESERVADO:
          raise ValueError("Solo se pueden cancelar turnos reservados.")
     
     turno.estado = Turno.CANCELADO
     turno.save(update_fields=["estado"])

     return turno