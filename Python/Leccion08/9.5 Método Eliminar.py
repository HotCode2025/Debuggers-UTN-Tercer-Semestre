 @classmethod
  def eliminar(cls, persona):
    with Conexion.obtenerConexion():
      with Conexion.obtenerCursor() as cursor:
        valores = (persona.id_persona,)
        cursor.execute(cls._ELIMINAR, valores)
        log.debug(f'Los objetos eliminados son: {persona}')
        return cursor.rowcount
