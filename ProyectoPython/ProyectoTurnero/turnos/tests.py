from django.test import TestCase

# Create your tests here.

from datetime import date, time, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from .models import (
    Ciudad,
    Disponibilidad,
    Especialidad,
    Establecimiento,
    Profesional,
    ProfesionalEstablecimientoEspecialidad,
    Turno,
    PerfilUsuario,
)

from .services import (
    cancelar_turno,
    obtener_horarios_disponibles,
    reservar_turno,
)


def proximo_dia_semana(dia_semana):
    hoy = date.today()
    diferencia = (dia_semana - hoy.weekday()) % 7
    diferencia = diferencia or 7
    return hoy + timedelta(days=diferencia)


class TurnoServiceTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="paciente_test",
            password="clave123",
        )

        self.ciudad = Ciudad.objects.create(
            nombre="Cordoba",
            provincia="Cordoba",
        )

        self.establecimiento = Establecimiento.objects.create(
            nombre="Clinica Test",
            tipo=Establecimiento.PRIVADO,
            direccion="Calle 123",
            ciudad=self.ciudad,
        )

        self.especialidad = Especialidad.objects.create(
            nombre="Cardiologia"
        )

        self.profesional = Profesional.objects.create(
            nombre="Ana",
            apellido="Lopez",
            matricula="TEST123",
        )

        ProfesionalEstablecimientoEspecialidad.objects.create(
            profesional=self.profesional,
            establecimiento=self.establecimiento,
            especialidad=self.especialidad,
        )

        Disponibilidad.objects.create(
            profesional=self.profesional,
            establecimiento=self.establecimiento,
            especialidad=self.especialidad,
            dia_semana=0,
            hora_inicio=time(8, 0),
            hora_fin=time(10, 0),
            duracion_turno_minutos=30,
        )

        self.fecha_lunes = proximo_dia_semana(0)

    def test_genera_horarios_disponibles(self):
        horarios = obtener_horarios_disponibles(
            self.profesional,
            self.establecimiento,
            self.especialidad,
            self.fecha_lunes,
        )

        self.assertEqual(
            horarios,
            [
                time(8, 0),
                time(8, 30),
                time(9, 0),
                time(9, 30),
            ],
        )

    def test_reservar_turno_ocupa_horario(self):
        reservar_turno(
            self.usuario,
            self.profesional,
            self.establecimiento,
            self.especialidad,
            self.fecha_lunes,
            time(8, 0),
        )

        horarios = obtener_horarios_disponibles(
            self.profesional,
            self.establecimiento,
            self.especialidad,
            self.fecha_lunes,
        )

        self.assertNotIn(time(8, 0), horarios)

    def test_no_permite_fecha_pasada(self):
        fecha_pasada = date.today() - timedelta(days=1)

        with self.assertRaisesMessage(
            ValueError,
            "No se pueden reservar turnos para fechas pasadas",
        ):
            reservar_turno(
                self.usuario,
                self.profesional,
                self.establecimiento,
                self.especialidad,
                fecha_pasada,
                time(8, 0),
            )

    def test_no_permite_fin_de_semana(self):
        fecha_sabado = proximo_dia_semana(5)

        with self.assertRaisesMessage(
            ValueError,
            "No se pueden reservar turnos para fines de semana",
        ):
            reservar_turno(
                self.usuario,
                self.profesional,
                self.establecimiento,
                self.especialidad,
                fecha_sabado,
                time(8, 0),
            )

    def test_cancelar_libera_y_permite_reservar_nuevamente(self):
        turno = reservar_turno(
            self.usuario,
            self.profesional,
            self.establecimiento,
            self.especialidad,
            self.fecha_lunes,
            time(8, 0),
        )

        cancelar_turno(self.usuario, turno)

        nuevo_turno = reservar_turno(
            self.usuario,
            self.profesional,
            self.establecimiento,
            self.especialidad,
            self.fecha_lunes,
            time(8, 0),
        )

        self.assertEqual(nuevo_turno.estado, Turno.RESERVADO)

class AutenticacionYPermisosAPITests(APITestCase):
    def setUp(self):
        self.paciente = User.objects.create_user(
            username="paciente_api",
            password="clave123",
            email="paciente@test.com",
        )
        PerfilUsuario.objects.create(
            usuario=self.paciente,
            rol=PerfilUsuario.PACIENTE,
        )

        self.medico_user = User.objects.create_user(
            username="medico_api",
            password="clave123",
            email="medico@test.com",
        )
        PerfilUsuario.objects.create(
            usuario=self.medico_user,
            rol=PerfilUsuario.MEDICO,
        )

        self.profesional = Profesional.objects.create(
            usuario=self.medico_user,
            nombre="Maria",
            apellido="Perez",
            matricula="API123",
        )

    def test_login_jwt_devuelve_rol_paciente(self):
        respuesta = self.client.post(
            reverse("token_obtain_pair"),
            {
                "username": "paciente_api",
                "password": "clave123",
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertIn("access", respuesta.data)
        self.assertIn("refresh", respuesta.data)
        self.assertEqual(respuesta.data["usuario"]["rol"], PerfilUsuario.PACIENTE)

    def test_paciente_no_puede_acceder_a_ruta_medica(self):
        self.client.force_authenticate(user=self.paciente)

        respuesta = self.client.get(
            reverse("medico_mis_turnos")
        )

        self.assertEqual(
            respuesta.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_medico_puede_acceder_a_sus_turnos(self):
        self.client.force_authenticate(user=self.medico_user)

        respuesta = self.client.get(
            reverse("medico_mis_turnos")
        )

        self.assertEqual(
            respuesta.status_code,
            status.HTTP_200_OK,
        )

    def test_medico_no_puede_acceder_a_ruta_de_paciente(self):
        self.client.force_authenticate(user=self.medico_user)

        respuesta = self.client.get(
            reverse("listar_mis_turnos")
        )

        self.assertEqual(
            respuesta.status_code,
            status.HTTP_403_FORBIDDEN,
        )