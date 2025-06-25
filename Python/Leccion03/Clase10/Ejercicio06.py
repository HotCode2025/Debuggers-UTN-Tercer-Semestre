
# Ejercicio 6 - Ingresar N enteros y visualizar la suma de los pares,
#               cuantos pares hay y cual es el promedio de los impares
# Inicializar variables
sumaPares = 0
contadorPares = 0
sumaImpares = 0
contadorImpares = 0

# Pedir la cantidad de números
nElementos = int(input("¿Cuántos números deseas ingresar?: "))

# Leo los números
for _ in range(nElementos):
    num = int(input("Introduce un número entero: "))
    if num % 2 == 0:  #  par
        sumaPares += num
        contadorPares += 1
    else:  # impar
        sumaImpares += num
        contadorImpares += 1

# Mostrar resultados
if contadorPares > 0:
    print(f"\nSuma de los números pares: {sumaPares}")
    print(f"Cantidad de números pares: {contadorPares}")
else:
    print("\nNo se han ingresado números pares")

if contadorImpares > 0:
    promedioImpares = sumaImpares / contadorImpares if contadorImpares > 0 else 0
    print(f"El promedio de los números impares: {promedioImpares:.2f}")
else:
    print("\nNo se han ingresado números impares")