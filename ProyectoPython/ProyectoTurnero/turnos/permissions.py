from rest_framework.permissions import BasePermission

from .models import PerfilUsuario

class EsPaciente(BasePermission):
    message = "Esta accion requiere un perfil de paciente."

    def has_permission(self, request, view):
        perfil = getattr(request.user, "perfil", None)
        return perfil is not None and perfil.rol == PerfilUsuario.PACIENTE
    
class EsMedico(BasePermission):
    message = "Esta accion requiere un perfil medico."

    def has_permission(self, request, view):
        perfil = getattr(request.user, "perfil", None)

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