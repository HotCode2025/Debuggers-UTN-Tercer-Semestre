import psycopg2 as bd
from logger_base import log
from psycopg2 import pool #Se importa 'pool' de psycopg2 para manejar el grupo de conexiones

class Conexion:
    # Atributos de configuración de la base de datos
    _DATABASE: str = "test_bd"
    _USERNAME: str = "postgres"
    _PASSWORD: str = "admin"
    _DB_PORT: str = "5432"
    _HOST: str = "127.0.0.1"
    # Parámetros del Pool: mínimo 1 conexión abierta, máximo 5 simultáneas
    _MIN_CON = 1
    _MAX_CON = 5
    _poll = None # Acá se guardará el objeto del Pool una vez creado

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def obtenerCursor(cls):
        pass
    @classmethod
    def crearConexion(cls):
        pass
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                  cls._MAX_CON,
                                                  host=cls._HOST,
                                                  user=cls._USERNAME,
                                                  password=cls._PASSWORD,
                                                  port=cls._DB_PORT,
                                                  database=cls._DATABASE)
                log.debug(f'creacion del pool exitosa: {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool
if __name__ == "__main__":
    pass