"""Validación y representación JSON de los recursos expuestos por la API."""

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from .models import(
    Ciudad,
    Establecimiento,
    Especialidad,
    Profesional,
    Turno,
    Disponibilidad,
    PerfilUsuario,
)

# Serializers de lectura para los catálogos y relaciones que consume Vue.
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

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

# Valida el formulario público y crea las dos entidades necesarias para un
# paciente: la cuenta autenticable de Django y su perfil de dominio.
class RegistroPacienteSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    nombre = serializers.CharField(max_length=150)
    apellido = serializers.CharField(max_length=150)
    tipo_documento = serializers.CharField(max_length=20)
    documento = serializers.CharField(max_length=30)
    genero = serializers.CharField(max_length=30, required=False, allow_blank=True)
    provincia = serializers.CharField(max_length=100, required=False, allow_blank=True)
    ciudad = serializers.CharField(max_length=100, required=False, allow_blank=True)
    telefono = serializers.CharField(max_length=30, required=False, allow_blank=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_username(self, value):
        username = value.strip()
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("El nombre de usuario ya se encuentra registrado.")
        return username

    def validate_documento(self, value):
        documento = value.strip()
        if PerfilUsuario.objects.filter(documento=documento).exists():
            raise serializers.ValidationError("El documento ya se encuentra registrado.")
        return documento

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("El correo electronico ya se encuentra registrado.")
        return email

    def validate_password(self, value):
        # Reutiliza las políticas configuradas por Django en settings.py.
        validate_password(value)
        return value

    @transaction.atomic
    def create(self, validated_data):
        """Crea el usuario y su perfil en una sola transacción."""
        password = validated_data.pop("password")
        documento = validated_data["documento"]

        user = User.objects.create_user(
            username=validated_data["username"],
            password=password,
            email=validated_data["email"],
            first_name=validated_data["nombre"].strip(),
            last_name=validated_data["apellido"].strip(),
        )

        PerfilUsuario.objects.create(
            usuario=user,
            rol=PerfilUsuario.PACIENTE,
            tipo_documento=validated_data["tipo_documento"],
            documento=documento,
            genero=validated_data.get("genero", ""),
            provincia=validated_data.get("provincia", ""),
            ciudad=validated_data.get("ciudad", ""),
            telefono=validated_data.get("telefono", ""),
        )
        return user

class DisponibilidadSerializer(serializers.ModelSerializer):
    # Las relaciones anidadas permiten mostrar nombres en el frontend sin
    # realizar consultas adicionales por cada identificador recibido.
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
    usuario = UsuarioSerializer(read_only=True)
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
        
# Amplía la respuesta estándar de SimpleJWT con los datos que el frontend
# necesita para decidir la pantalla inicial y conservar la sesión visual.
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        perfil = getattr(self.user, "perfil", None)

        data["usuario"] = {
            "id": self.user.id,
            "username": self.user.username,
            "nombre": self.user.get_full_name() or self.user.username,
            "email": self.user.email,
            "dni": perfil.documento if perfil else "",
            "tel": perfil.telefono if perfil else "",
            "rol": perfil.rol if perfil else None,
        }

        return data
