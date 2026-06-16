from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.provincia}"

class Establecimiento(models.Model):
    PUBLICO = "PUBLICO"
    PRIVADO= "PRIVADO"

    TIPO_CHOICES = [
        (PUBLICO, "Público"),
        (PRIVADO, "Privado"),
    ]

    nombre = models.CharField(max_length=150)
    tipo= models.CharField(max_length=20, choices=TIPO_CHOICES)
    direccion = models.CharField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name="establecimientos")
    
    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class EstablecimientoEspecialidad(models.Model):
    establecimiento = models.ForeignKey(
        Establecimiento,
        on_delete=models.CASCADE,
        related_name="especialidades_disponibles"
    )
    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        related_name="establecimientos_con_especialidad"
    )

    class Meta:
        unique_together = ("establecimiento", "especialidad")
    
    def __str__(self):
        return f"{self.establecimiento} - {self.especialidad}"
    
class Profesional(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    matricula = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class ProfesionalEstablecimientoEspecialidad(models.Model):
    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name="lugares_atencion"
    )
    establecimiento = models.ForeignKey(
        Establecimiento,
        on_delete=models.CASCADE,
        related_name="profesionales"
    )
    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        related_name="profesionales"
    )

    class Meta:
        unique_together = ("profesional", "establecimiento","especialidad")
    
    def __str__(self):
        return f"{self.profesional} - {self.establecimiento} -{self.especialidad}"
    
class Disponibilidad(models.Model):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4

    DIA_SEMANA_CHOICES = [
        (LUNES, "Lunes"),
        (MARTES, "Martes"),
        (MIERCOLES, "Miércoles"),
        (JUEVES, "Jueves"),
        (VIERNES, "Viernes"),
    ]

    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name="disponibilidades"
    )

    establecimiento = models.ForeignKey(
        Establecimiento,
        on_delete=models.CASCADE,
        related_name="disponibilidades"
    )

    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        related_name="disponibilidades"
    )
    
    dia_semana = models.IntegerField(choices=DIA_SEMANA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    duracion_turno_minutos = models.PositiveBigIntegerField(default=30)

    def __str__(self):
        return f"{self.profesional} - {self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}"
    
class Turno(models.Model):
    RESERVADO = "RESERVADO"
    CANCELADO = "CANCELADO"
    ATENDIDO = "ATENDIDO"

    ESTADO_CHOICES = [
        (RESERVADO, "Reservado"),
        (CANCELADO, "Cancelado"),
        (ATENDIDO, "Atendido"),
    ]

    usuario = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name="turnos"
    )

    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name="turnos"
    )

    establecimiento = models.ForeignKey(
        Establecimiento,
        on_delete=models.CASCADE,
        related_name="turnos"
    )

    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        related_name="turnos"
    )

    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=RESERVADO)

    class Meta:
        unique_together = ("profesional", "establecimiento", "especialidad", "fecha", "hora")

        def __str__(self):
            return f"Turno de {self.usuario} con {self.profesional} en {self.establecimiento} para {self.especialidad} el {self.fecha} a las {self.hora} - Estado: {self.estado}"
        

   

