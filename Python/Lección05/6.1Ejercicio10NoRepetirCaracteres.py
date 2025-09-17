# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

cadena = input("Ingresa una cadena de texto: ") # Pedimos la cadena

sin_repetir = list(set(cadena)) # La funcion set elimina los caracteres duplicados de la lista
print(sin_repetir)
