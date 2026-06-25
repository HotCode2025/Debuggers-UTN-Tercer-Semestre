"""Permisos por rol utilizados para proteger los endpoints REST."""

from rest_framework.permissions import BasePermission

from .models import PerfilUsuario

# Permisos declarativos: cada vista indica el rol autorizado y DRF ejecuta
# estas comprobaciones antes de entrar en la función del endpoint.
class EsPaciente(BasePermission):
    message = "Esta accion requiere un perfil de paciente."

    def has_permission(self, request, view):
        perfil = getattr(request.user, "perfil", None)
        return perfil is not None and perfil.rol == PerfilUsuario.PACIENTE
    
class EsMedico(BasePermission):
    message = "Esta accion requiere un perfil medico."

    def has_permission(self, request, view):
        perfil = getattr(request.user, "perfil", None)

        # Además del rol, se exige la relación Profesional para evitar cuentas
        # médicas incompletas que no podrían administrar una agenda.
        return(
            perfil is not None
            and perfil.rol == PerfilUsuario.MEDICO
            and hasattr(request.user,"perfil_profesional")
        )
    
class EsAdministrador(BasePermission):
    message = "Esta accion requiere permisos de administrador."

    def has_permission(self, request, view):
        perfil = getattr(request.user,"perfil",None)

        return(
            request.user.is_superuser 
            or (
                perfil is not None
                and perfil.rol ==PerfilUsuario.ADMIN
             )
        )
