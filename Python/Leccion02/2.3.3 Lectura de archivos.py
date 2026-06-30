
archivo = open('prueba.txt', 'r', encoding='utf8')  # la r es de leer

# print(archivo.read()) # muestra toda la informacion

# print(archivo.read(15)) # muestra los primeros n caracteres
# print(archivo.read(10)) # muestra los siguientes n caracteres

print(archivo.readline()) # Lee la linea desde donde esta el cursor hasta el final
