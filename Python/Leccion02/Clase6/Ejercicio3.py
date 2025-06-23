"""Ejercicio 3
Intercambiar el valor de dos variables"""
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
temp = a
a = b
b = temp
print(f"El nuevo valor de A es: ",a)
print(f"El nuevo valor de b es: ",b)
