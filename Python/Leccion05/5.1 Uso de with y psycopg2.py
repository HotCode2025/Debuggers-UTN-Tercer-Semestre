# Clase 05
# 5.1 Uso de with y psycopg2

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall() # Recuperamos todos los registros que serán una lista

            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
#finally:
    #conexion.close()