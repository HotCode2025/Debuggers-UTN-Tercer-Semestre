"""Rutas funcionales de pacientes y profesionales."""

from django.urls import path

from . import views


# Las rutas siguen el recorrido público, las acciones del paciente y el panel
# médico. Los permisos específicos permanecen declarados en cada vista.
urlpatterns = [
    path("auth/registro/", views.registrar_paciente, name="registrar_paciente"),
    path("ciudades/", views.listar_ciudades, name="listar_ciudades"),
    path("establecimientos/", views.listar_establecimientos, name="listar_establecimientos"),
    path("especialidades/", views.listar_especialidades, name="listar_especialidades"),
    path("profesionales/", views.listar_profesionales, name="listar_profesionales"),
    path("horarios-disponibles/", views.listar_horarios_disponibles, name="listar_horarios_disponibles"),
    path("turnos/reservar/", views.reservar_turno_view, name="reservar_turno"),
    path("mis-turnos/", views.listar_mis_turnos, name="listar_mis_turnos"),
    path("mis-turnos/activos/", views.listar_mis_turnos_activos, name="listar_mis_turnos_activos"),
    path("turnos/<int:turno_id>/cancelar/", views.cancelar_turno_view, name="cancelar_turno"),
    path("medico/mis_turnos/",views.medico_mis_turnos,name="medico_mis_turnos"),
    path("medico/mis_turnos/activos/",views.medico_mis_turnos_activos, name="medico_mis_turnos_activos"),
    path("medico/agenda/",views.medico_agenda_por_fecha, name="medico_agenda_por_fecha"),
    path("medico/disponibilidades/", views.medico_mis_disponibilidades, name= "medico_mis_disponibilidades"),
    path("medico/disponibilidades/crear/", views.medico_crear_disponibilidad, name="medico_crear_disponibilidades"),
    path("medico/disponibilidades/<int:disponibilidad_id>/modificar/", views.medico_modificar_disponibilidad, name= "medico_modificar_disponibilidad"),
    path("medico/disponibilidades/<int:disponibilidad_id>/eliminar/", views.medico_eliminar_disponibilidad, name="medico_eliminar_disponibilidad"),
    path("medico/turnos/<int:turno_id>/atendido/", views.medico_marcar_turno_atendido, name="medico_marcar_turno_atendido"),
    path("medico/turnos/<int:turno_id>/cancelar/", views.medico_cancelar_turno, name="medico_cancelar_turno",)
]
