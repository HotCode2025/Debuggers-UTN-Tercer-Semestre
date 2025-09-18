# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados cesius
# a fahrenheit y viseversa.
# Investigar las formulas

# Formula de Celsius a Fahrenheit. F = (C * 9 / 5) + 32
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Formula de fahrenheit a celsius. C = (F - 32) * 5 / 9
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 /9
    return celsius

# Menu
while True:
    print("\n--- Convertidor de Temperaturas ---")
    print("1. De Celsius a Fahrenheint")
    print("2. De Fahrenheit a Celsius")
    print("0. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C es igual a {fahrenheit}°F")
        elif opcion == 2:
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F es igual a {celsius}°C")
        elif opcion == 0:
            break
        else:
            print("Error. Las opciones validas son 1 o 2")
    except ValueError:
        print("Error. Por favor, ingrese un numero.")
