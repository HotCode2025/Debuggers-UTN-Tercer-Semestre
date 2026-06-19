# API Turnero Médico

Base local: `http://127.0.0.1:8000/api/`

## Autenticación

### Iniciar sesión
POST `auth/login/`

```json
{
  "username": "usuario",
  "password": "contraseña"
}

DEVUELVE ACCESS, REFRESH Y LOS DATOS DEL USUARIO CON SU ROL

## RENOVAR TOKEN

POST auth/refresh/
{
  "refresh": "TOKEN_REFRESH"
}

Las rutas protegidas requieren: Authorization: Bearer TOKEN_ACCESS

## CONSULTAS PUBLICAS

- GET ciudades/
- GET establecimientos/?ciudad_id=1
- GET especialidades/?establecimiento_id=1
- GET profesionales/?establecimiento_id=1&especialidad_id=1
- GET horarios-disponibles/?profesional_id=1&establecimiento_id=1&especialidad_id=1&fecha=2026-06-22

## Paciente

POST turnos/reservar/
GET mis-turnos/
GET mis-turnos/activos/
POST turnos/{id}/cancelar/

### Reservar turno
{
  "profesional_id": 1,
  "establecimiento_id": 1,
  "especialidad_id": 1,
  "fecha": "2026-06-22",
  "hora": "08:30"
}

## Medico

- GET medico/mis_turnos/
- GET medico/mis_turnos/activos/
- GET medico/agenda/?fecha=2026-06-22
- GET medico/disponibilidades/
- POST medico/disponibilidades/crear/
- PUT medico/disponibilidades/{id}/modificar/
- DELETE medico/disponibilidades/{id}/eliminar/
- POST medico/turnos/{id}/atendido/
- POST medico/turnos/{id}/cancelar/

### Crear o modificar disponibilidad

{
  "establecimiento_id": 1,
  "especialidad_id": 1,
  "dia_semana": 0,
  "hora_inicio": "08:00",
  "hora_fin": "12:00",
  "duracion_turno_minutos": 30
}

Dias: Lunes (0), Martes (1), Miercoles (2), Jueves (3), Viernes(4).
