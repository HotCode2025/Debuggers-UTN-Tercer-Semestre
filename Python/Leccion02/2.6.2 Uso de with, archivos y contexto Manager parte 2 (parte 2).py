# 1.6 Uso de with, archivos y contexto Manager Parte 2


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())