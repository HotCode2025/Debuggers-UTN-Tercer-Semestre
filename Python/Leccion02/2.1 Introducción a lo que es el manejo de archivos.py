#para abrir un archivo declaramos una variable

try:
    archivo = open('prueba.txt','w') #sirve para abrir un archivo. Si existe lo toma, sino lo crea. la W significa write, que es escribir.
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close #con esto se debe cerrar el archivo
#puede arrojar una excepcion, por eso el try
#una vez terminado y ejecutado, se crea el archivo prueba.txt en la carpeta
