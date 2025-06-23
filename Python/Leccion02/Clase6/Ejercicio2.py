""" Ejercicio 2: Deerminar la losolucion logica de
la siguiente expresion
    ((3+5*8)<3 and ((-6/3+4)+2<2) or (a>b)
1. Pedir al usuario los dos valores para a y b
2. Escribir en codigo la siguiente expresion
3. Mostrar el resultado"""

a = float(input("Digite el valor para a: "))
b = float(input("Digite el valor para b: "))
resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)
print(f"El resultado es: {resultado}")