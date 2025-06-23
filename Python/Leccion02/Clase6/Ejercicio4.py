"""Ejercicio 4: Area y longitud de un circulo
Hacer un programa para ingresar el radio de un circulo
y se reporte su area y la longitud de la circunferencia"""

import math
# Define el radio
radio = float(input("Ingrese el radio del circulo: "))

# Calcula area y longitud
area = math.pi * radio ** 2
circunferencia = 2 * math.pi * radio

# Mostrar resultados
print(f"Area: {area:.2f}")
print(f"Circunferencia: {circunferencia:.2f}")
