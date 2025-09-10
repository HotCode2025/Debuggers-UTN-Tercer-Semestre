# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10, luego modificar los
# elementos de la lista multiplicando por un valor ingresado por el usuario

lista = list(range(1, 11))
print('Lista original: ', lista)

multiplicador = int(input('Ingrese un número para multiplicar la lista: '))

for i in range(len(lista)):
    lista[i] = lista[i] * multiplicador
print('Lista modificada: ', lista)
