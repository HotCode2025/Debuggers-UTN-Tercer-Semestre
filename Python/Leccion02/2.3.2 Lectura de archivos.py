
archivo = open('prueba.txt', 'r', encoding='utf8')  # la r es de leer

# print(archivo.read())
print(archivo.read(15)) # muestra n caracteres

print(archivo.readline()) # Lee la linea desde donde esta el cursor hasta el final
