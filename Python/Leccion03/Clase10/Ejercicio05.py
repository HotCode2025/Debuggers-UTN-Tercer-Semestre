 # Ejercicio 5
while True:
     numero = int(input("Ingresa el numero del cual deseas obtener el facorial: "))
     if numero >= 0:
         break
     else:
         print("El numero debe ser mayor a Cero")

factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es {factorial} ")

import math
print(f"El factorial de {numero} es {math.factorial(numero)}")