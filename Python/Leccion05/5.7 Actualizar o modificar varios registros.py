# 5.7 Actualizar o modificar varios registros

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin123',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Jorge', 'Rolo', 'jrolo@gmail.com', 7),
                    ('Rowi', 'Costa', 'rcosts@gmail.com', 8),
                    ('Wili', 'Moreno', 'morenow@gmail.con', 9)
            ) # Es una tupla de tuplas
            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount

            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()