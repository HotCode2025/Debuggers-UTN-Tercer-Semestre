# 7.2 Argumentos variables para un diccionario

def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # Kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy Key')
listarTerminos(Nombre='Lionel Messi')

# 7.3 Lista de elementos con funciones(convertir)

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla, en un solo elemnto no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista

# 7.4 Funciones recursivas con factorial(hacer la tarea)
# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero -1) # Caso recursivo

resultado = factorial(5) # Lo hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}') # Tarea que el usuario ingrese el numero para calcular el factorial
