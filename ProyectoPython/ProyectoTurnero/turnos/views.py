from django.shortcuts import render
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import EsMedico, EsPaciente

from .models import (
    Ciudad,
    Establecimiento,
    Especialidad,
    Profesional,
    Turno,
    Disponibilidad,
)

from .serializers import (
    CiudadSerializer,
    EstablecimientoSerializer,
    EspecialidadSerializer,
    ProfesionalSerializer,
    TurnoSerializer,
    DisponibilidadSerializer,
) 

from .services import (
    obtener_establecimientos_por_ciudad,
    obtener_especialidades_por_establecimiento,
    obtener_profesionales_por_establecimiento_y_especialidad,
    obtener_horarios_disponibles,
    reservar_turno,
    obtener_turnos_de_usuario,
    obtener_turnos_activos_de_usuario,
    cancelar_turno,
    obtener_profesional_de_usuario,
    obtener_turnos_de_profesional,
    obtener_turnos_activos_de_profesional,
    obtener_turnos_de_profesional_por_fecha,
    obtener_disponibilidades_de_profesional,
    crear_disponibilidad_profesional,
    modificar_disponibilidad_profesional,
    eliminar_disponibilidad_profesional,
    marcar_turno_como_atendido,
    cancelar_turno_como_profesional,
)

@api_view(["GET"])
def listar_ciudades(request):
    ciudades = Ciudad.objects.all().order_by("nombre")
    serializer = CiudadSerializer(ciudades, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def listar_establecimientos(request):
    ciudad_id = request.query_params.get("ciudad_id")

    if not ciudad_id:
        return Response(
            {"error": "Debe enviar ciudad_id"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try: 
        ciudad = Ciudad.objects.get(id=ciudad_id)
    except ciudad.DoesNotExist:
        return Response(
            {"error":"La ciudad indicada no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    establecimientos = obtener_establecimientos_por_ciudad(ciudad)
    serializer = EstablecimientoSerializer(establecimientos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def listar_especialidades(request):
    establecimiento_id = request.query_params.get("establecimiento_id")

    if not establecimiento_id:
        return Response(
            {"error": "Debe enviar establecimiento_id."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    try:
        establecimiento = Establecimiento.objects.get(id=establecimiento_id)
    except Establecimiento.DoesNotExist:
        return Response(
            {"error": "El establecimiento indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    especialidades = obtener_especialidades_por_establecimiento(establecimiento)
    serializer = EspecialidadSerializer(especialidades, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def listar_profesionales(request):
    establecimiento_id = request.query_params.get("establecimiento_id")
    especialidad_id = request.query_params.get("especialidad_id")

    if not establecimiento_id or not especialidad_id:
        return Response(
            {"error": "Debe enviar establecimiento_id y especialidad_id."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try: 
        establecimiento = Establecimiento.objects.get(id=establecimiento_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)
    except Establecimiento.DoesNotExist:
        return Response(
            {"error":"El establecimiento indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Especialidad.DoesNotExist:
        return Response(
            {"error":"La especialidad indicada no existe."},
            status=status.HTTP_404_NOT_FOUND,
            )
    profesionales = obtener_profesionales_por_establecimiento_y_especialidad(
        establecimiento,
        especialidad,
    )
    serializer = ProfesionalSerializer(profesionales, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def listar_horarios_disponibles(request):
    profesional_id= request.query_params.get("profesional_id")
    establecimiento_id = request.query_params.get("establecimiento_id")
    especialidad_id = request.query_params.get("especialidad_id")
    fecha_texto = request.query_params.get("fecha")

    if not profesional_id or not establecimiento_id or not especialidad_id or not fecha_texto:
        return Response(
            {
                "error": (
                    "Debe enviar profesional_id, establecimiento_id,"
                    "especialidad_id y fecha."
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        profesional = Profesional.objects.get(id=profesional_id)
        establecimiento = Establecimiento.objects.get(id=establecimiento_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)
        fecha = datetime.strptime(fecha_texto,"%Y-%m-%d").date()
    except Profesional.DoesNotExist:
        return Response(
            {"error":"El profesional indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Establecimiento.DoesNotExist:
        return Response(
            { "error": "El Profesional indicado no existe"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Especialidad.DoesNotExist:
        return Response(
            {"error": "La especialidad indicada no existe"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValueError:
        return Response(
            {
                "error": "La fecha debe tener el formato YYYY-MM-DD."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    horarios = obtener_horarios_disponibles(
        profesional,
        establecimiento,
        especialidad,
        fecha,
    )

    return Response([horario.strftime("%H:%M")for horario in horarios])

@api_view(["POST"])
@permission_classes([IsAuthenticated, EsPaciente])
def reservar_turno_view(request):
    profesional_id = request.data.get("profesional_id")
    establecimiento_id = request.data.get("establecimiento_id")
    especialidad_id = request.data.get("especialidad_id")
    fecha_texto = request.data.get("fecha")
    hora_texto = request.data.get("hora")

    if not profesional_id or not establecimiento_id or not especialidad_id or not fecha_texto or not hora_texto:
        return Response(
            {
                "error": (
                    "Debe enviar profesional_id, establecimiento_id, "
                    "especialidad_id, fecha y hora."
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        profesional = Profesional.objects.get(id=profesional_id)
        establecimiento = Establecimiento.objects.get(id=establecimiento_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)
        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
        hora = datetime.strptime(hora_texto, "%H:%M").time()
    except Profesional.DoesNotExist:
        return Response(
            {"error": "El profesional indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Establecimiento.DoesNotExist:
        return Response(
            {"error": "El establecimiento indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Especialidad.DoesNotExist:
        return Response(
            {"error": "La especialidad indicada no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValueError:
        return Response(
            {"error": "La fecha debe ser YYYY-MM-DD y la hora HH:MM."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        turno = reservar_turno(
            usuario=request.user,
            profesional=profesional,
            establecimiento=establecimiento,
            especialidad=especialidad,
            fecha=fecha,
            hora=hora,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = TurnoSerializer(turno)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes([IsAuthenticated, EsPaciente])
def listar_mis_turnos(request):
    turnos = obtener_turnos_de_usuario(request.user)
    serializer = TurnoSerializer(turnos, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated, EsPaciente])
def listar_mis_turnos_activos(request):
    turnos = obtener_turnos_activos_de_usuario(request.user)
    serializer = TurnoSerializer(turnos, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated, EsPaciente])
def cancelar_turno_view(request, turno_id):
    try:
        turno = Turno.objects.get(id=turno_id)
    except Turno.DoesNotExist:
        return Response(
            {"error": "El turno indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        turno = cancelar_turno(request.user, turno)
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = TurnoSerializer(turno)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated,EsMedico])
def medico_mis_turnos(request):
    try: 
        profesional = obtener_profesional_de_usuario(request.user)
    except ValueError as error:
        return Response(
            {"error":str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    turnos = obtener_turnos_de_profesional(profesional)
    serializer = TurnoSerializer(turnos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated,EsMedico])
def medico_mis_turnos_activos(request):
    try:
        profesional = obtener_profesional_de_usuario(request.user)
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    turnos = obtener_turnos_activos_de_profesional(profesional)
    serializer = TurnoSerializer(turnos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated,EsMedico])

def medico_agenda_por_fecha(request):
    fecha_texto = request.query_params.get("fecha")

    if not fecha_texto:
        return Response(
            {"error": "Debe enviar fecha."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    try:
        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
    except ValueError:
        return Response(
            {"error": "La fecha debe tener formato YYYY-MM-DD."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try: 
        profesional = obtener_profesional_de_usuario(request.user)
        turnos = obtener_turnos_de_profesional_por_fecha(profesional, fecha)
    except ValueError as error:
        return Response(
            {"error":str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    serializer = TurnoSerializer(turnos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated,EsMedico])
def medico_mis_disponibilidades(request):
    try:
        profesional = obtener_profesional_de_usuario(request.user)
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    disponibilidades = obtener_disponibilidades_de_profesional(profesional)
    serializer = DisponibilidadSerializer(disponibilidades, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated,EsMedico])
def medico_crear_disponibilidad(request):
    establecimiento_id = request.data.get("establecimiento_id")
    especialidad_id = request.data.get("especialidad_id")
    dia_semana = request.data.get("dia_semana")
    hora_inicio_texto = request.data.get("hora_inicio")
    hora_fin_texto = request.data.get("hora_fin")
    duracion_turno_minutos = request.data.get("duracion_turno_minutos")

    if (
        not establecimiento_id
        or not especialidad_id
        or dia_semana is None
        or not hora_inicio_texto
        or not hora_fin_texto
        or not duracion_turno_minutos
    ):
        return Response(
            {
                "error": (
                    "Debe enviar establecimiento_id,especialidad_id, dia_semana,"
                    "hora_inicio, hora_fin y duracion_turno_minutos."
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        profesional = obtener_profesional_de_usuario(request.user)
        establecimiento = Establecimiento.objects.get(id=establecimiento_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)
        dia_semana = int(dia_semana)
        duracion_turno_minutos= int(duracion_turno_minutos)
        hora_inicio = datetime.strptime(hora_inicio_texto,"%H:%M").time()
        hora_fin = datetime.strptime(hora_fin_texto, "%H:%M").time()
    except ValueError as error:
        return Response(
            {"error":str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Establecimiento.DoesNotExist:
        return Response(
            {"error":"El establecimiento indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Especialidad.DoesNotExist:
        return Response(
            {"error":"La especialidad indicada no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    try:
        disponibilidad = crear_disponibilidad_profesional(
            profesional=profesional,
            establecimiento=establecimiento,
            especialidad=especialidad,
            dia_semana=dia_semana,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            duracion_turno_minutos=duracion_turno_minutos,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = DisponibilidadSerializer(disponibilidad)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
@permission_classes([IsAuthenticated, EsMedico])
def medico_modificar_disponibilidad(request,disponibilidad_id):
    establecimiento_id = request.data.get("establecimiento_id")
    especialidad_id = request.data.get("especialidad_id")
    dia_semana = request.data.get("dia_semana")
    hora_inicio_texto = request.data.get("hora_inicio")
    hora_fin_texto = request.data.get("hora_fin")
    duracion_turno_minutos = request.data.get("duracion_turno_minutos")

    if(
        not establecimiento_id
        or not especialidad_id
        or dia_semana is None
        or not hora_inicio_texto
        or not hora_fin_texto
        or not duracion_turno_minutos
    ):
        return Response(
            {
                "error":(
                    "Debe enviar establecimiento_id, especialidad_id, dia_semana,"
                    "hora_inicio, hora_fin y duracion_turno_minutos."
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        disponibilidad = Disponibilidad.objects.get(id=disponibilidad_id)
        profesional = obtener_profesional_de_usuario(request.user)
        establecimiento = Establecimiento.objects.get(id=establecimiento_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)
        dia_semana = int(dia_semana)
        duracion_turno_minutos = int(duracion_turno_minutos)
        hora_inicio = datetime.strptime(hora_inicio_texto, "%H:%M").time()
        hora_fin = datetime.strptime(hora_fin_texto,"%H:%M").time()
    except Disponibilidad.DoesNotExist:
        return Response(
            {"error": "La disponibilidad indicada no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Establecimiento.DoesNotExist:
        return Response(
            {"error": "El establecimiento indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        disponibilidad = modificar_disponibilidad_profesional(
            disponibilidad=disponibilidad,
            profesional=profesional,
            establecimiento=establecimiento,
            especialidad=especialidad,
            dia_semana=dia_semana,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            duracion_turno_minutos=duracion_turno_minutos,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = DisponibilidadSerializer(disponibilidad)
    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, EsMedico])
def medico_eliminar_disponibilidad(request,disponibilidad_id):
    try:
        disponibilidad = Disponibilidad.objects.get(id=disponibilidad_id)
        profesional = obtener_profesional_de_usuario(request.user)
    except Disponibilidad.DoesNotExist:
        return Response(
            {"error":"La disponibilidad indicada no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    try:
        eliminar_disponibilidad_profesional(disponibilidad,profesional)
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
@permission_classes([IsAuthenticated, EsMedico])
def medico_marcar_turno_atendido(request, turno_id):
    try:
        profesional = obtener_profesional_de_usuario(request.user)
        turno = Turno.objects.get(id=turno_id)
        turno = marcar_turno_como_atendido(turno, profesional)
    except Turno.DoesNotExist:
        return Response(
            {"error": "El turno indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(TurnoSerializer(turno).data)


@api_view(["POST"])
@permission_classes([IsAuthenticated, EsMedico])
def medico_cancelar_turno(request, turno_id):
    try:
        profesional = obtener_profesional_de_usuario(request.user)
        turno = Turno.objects.get(id=turno_id)
        turno = cancelar_turno_como_profesional(turno, profesional)
    except Turno.DoesNotExist:
        return Response(
            {"error": "El turno indicado no existe."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(TurnoSerializer(turno).data)



