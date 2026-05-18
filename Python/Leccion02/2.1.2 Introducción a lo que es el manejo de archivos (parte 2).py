#2.1.1 Introduccion al manejo de archivos
#para abrir un archivo declaramos una variable

try:
    archivo = open('prueba.txt','w') #sirve para abrir un archivo. Si existe lo toma, sino lo crea. la W significa write, que es escribir.
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close #con esto se debe cerrar el archivo
#puede arrojar una excepcion, por eso el try
#una vez terminado y ejecutado, se crea el archivo prueba.txt en la carpeta


#2.1.2 Introduccion al manejo de archivos parte 2

try:
    archivo = open('prueba.txt','w')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt. \n')
    archivo.write('Con esto terminamos,')
except Exception as e:
    print(e)
finally:
    archivo.close()

#repetimos el codigo de arriba para poder diferenciar dentro de la misma tematica las 2 tareas realizadas
#esto es posible sin inconvenientes gracias al archivo.close

