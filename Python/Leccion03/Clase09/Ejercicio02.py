# Ejercicio 2: Calcular la suma de "N" primeros numeros

N = int(input("Ingrese la cantidad de numeros a sumarse: "))

suma = 0

# Voy sumando en suma hasta llegar a N
for i in range(1, N + 1):
    suma += i
print(f"La suma de los primero {N} numeros es: {suma}")
