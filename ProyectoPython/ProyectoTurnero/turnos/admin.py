from django.contrib import admin

# Register your models here.

from .models import(
    Ciudad,
    Disponibilidad,
    Especialidad,
    Establecimiento,
    EstablecimientoEspecialidad,
    PerfilUsuario,
    Profesional,
    ProfesionalEstablecimientoEspecialidad,
    Turno,
)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","provincia")
    search_fields = ("nombre","provincia")

@admin.register(Establecimiento)
class EstablecimientoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","tipo","ciudad","direccion")
    list_filter = ("tipo","ciudad")
    search_fields = ("nombre","direccion")

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "matricula", "usuario")
    search_fields = ("nombre", "apellido", "matricula")


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "rol")
    list_filter = ("rol",)
    search_fields = ("usuario__username", "usuario__email")


@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "profesional",
        "establecimiento",
        "especialidad",
        "dia_semana",
        "hora_inicio",
        "hora_fin",
        "duracion_turno_minutos",
    )
    list_filter = ("dia_semana", "establecimiento", "especialidad")


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "profesional",
        "fecha",
        "hora",
        "estado",
    )
    list_filter = ("estado", "fecha", "especialidad", "establecimiento")
    search_fields = (
        "usuario__username",
        "profesional__nombre",
        "profesional__apellido",
    )


admin.site.register(EstablecimientoEspecialidad)
admin.site.register(ProfesionalEstablecimientoEspecialidad)
