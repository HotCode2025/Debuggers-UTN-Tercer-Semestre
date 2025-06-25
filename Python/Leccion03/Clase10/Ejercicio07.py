# Ejercicio 7- Dadas las horas trabajadas de 5 personas y el valor de la hora
#               Calcular el salario y la sumatoria de todos los salarios

sumatoriaSalarios = 0

for i in range(1, 6):
    cantidadHoras = float(input(f"Introduce las horas trabajadas por el empleado {i}: "))
    valorHora = float(input("Introduce el valor de la hora trabajada: "))
    salario = cantidadHoras * valorHora

    print(f"El salario de la persona {i} es: ${salario:.2f}")

    sumatoriaSalarios = sumatoriaSalarios + salario

print(f"\nLa sumatoria de todos los salarios es: ${sumatoriaSalarios:.2f}")