from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import(
    Ciudad,
    Establecimiento,
    Especialidad,
    Profesional,
    Turno,
    Disponibilidad,
)

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ["id", "nombre", "provincia"]

class EstablecimientoSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(read_only=True)

    class Meta: 
        model = Establecimiento
        fields = ["id", "nombre", "tipo","direccion","ciudad"]

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ["id", "nombre"]

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ["id", "nombre", "apellido", "matricula"]

class DisponibilidadSerializer(serializers.ModelSerializer):
    profesional=ProfesionalSerializer(read_only=True)
    establecimiento = EstablecimientoSerializer(read_only=True)
    especialidad = EspecialidadSerializer(read_only=True)

    class Meta: 
        model = Disponibilidad
        fields= [
            "id",
            "profesional",
            "establecimiento",
            "dia_semana",
            "hora_inicio",
            "hora_fin",
            "duracion_turno_minutos",
            "especialidad",
        ]

class TurnoSerializer(serializers.ModelSerializer):
    profesional = ProfesionalSerializer(read_only=True)
    establecimiento = EstablecimientoSerializer(read_only=True)
    especialidad = EspecialidadSerializer(read_only=True)

    class Meta:
        model = Turno
        fields = [
            "id",
            "usuario",
            "profesional",
            "establecimiento",
            "especialidad",
            "fecha",
            "hora",
            "estado",
        ]
        read_only_fields = ["usuario","estado"]
        
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        perfil = getattr(self.user, "perfil", None)

        data["usuario"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "rol": perfil.rol if perfil else None,
        }

        return data