# Ejercicio 3: Funcion Recursiva
#Imprimir numeros de 5 a 1 de manera descendiente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
#5
#4
#3
#2
#1
# En caso de ser el numero 3 debe imprimir:
#3
#2
#1
# Si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivo(numero - 1)
imprimir_numeros_recursivo(5)
print()
imprimir_numeros_recursivo(3)
print()
imprimir_numeros_recursivo(10)