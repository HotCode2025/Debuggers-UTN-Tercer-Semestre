# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hastael 10. Por ejemplo
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

# Tabla de multiplicar de un numero

numero = int(input("Ingresa un numero: "))

tabla = []
for i in range(1, 11):
    resultado = numero * i
    tabla.append(resultado)

print("La tabla de multiplicar es: ", tabla)
