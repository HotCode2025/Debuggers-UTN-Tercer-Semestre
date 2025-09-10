# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir numeros y meterlos en una lista hasta que el usuario introduzca el numero 0
# Por ultimo ordenar de menor a mayor y mostrar la lista

lista = []
numero = ''

while numero != 0:
    entrada = int(input("Ingresa un número (0 para teiminar): "))
    if entrada == 0:
        break
    lista.append(entrada)

# Ordenamos la lista de menor a mayor
lista.sort()
print("Lista oredenada: ", lista)
