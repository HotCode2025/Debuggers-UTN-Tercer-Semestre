# Ejercicio 1: Pedir que el usuario inrese un año y verificar si es bisiesto
while True:
    anio = int(input("Ingrese el año o 1 para salir: "))

# Verifico si quiere salir
    if anio == 1:
        print("Fin.")
        break

# Verifico si es bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} es bisiesto.")
    else:
        print(f"El año {anio} no es bisiesto")
