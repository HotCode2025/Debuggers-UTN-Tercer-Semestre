import psycopg2 as bd # Para conectarse con Postgre

conexion = bd.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    conexion.autocommit = False # Inicia la transaccion
    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUE (%s, %s, %s)' 
    valores = ('Jorge', 'Prol45678910', 'clara@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit # Commit manual - Se cierra la transaccion
    print(f'Termina la transaccion')

    registros_insertados = cursor.rowcount
    print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()
