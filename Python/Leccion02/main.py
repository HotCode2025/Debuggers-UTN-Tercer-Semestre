"""# Clase 6.1
# En esta clase veremos la sentecia if/else

condicion = True
if condicion == True:
    print("condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion sin especificar")"""

# Ejercicio: Convercion de numero a texto

num = int(input("Digite un numero en el rango de 1 al 3: "))
numTexto = " "
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f"El numero ingresado es: {num} - {numTexto}")

# Sintaxis simplificada (Operador Ternario)

condicion = True
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")
print("Condicion Verdadera") if condicion else print("Condicion Falsa")


