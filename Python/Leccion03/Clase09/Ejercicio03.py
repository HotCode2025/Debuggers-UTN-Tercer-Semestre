# Ejercicio 3: Leer 10 numeros e imprimir cuantos son positivos,
# cuantos negativos y cuantos neutros

positivos = 0
negativos = 0
neutros = 0

# Leer 10 numeros
for i in range(10):
    numero = int(input(f"Ingrese el numero {i + 1}: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

# Mostrar resultado
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de numeros neutros: {neutros}")