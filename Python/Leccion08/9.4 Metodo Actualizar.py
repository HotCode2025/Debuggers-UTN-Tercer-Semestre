# 9.4 Metodo Actualizar
@classmethod
def actualizar(cls, persona):
    with Conexion.obtenerConexion():
        with Conexion.obtenerCursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount