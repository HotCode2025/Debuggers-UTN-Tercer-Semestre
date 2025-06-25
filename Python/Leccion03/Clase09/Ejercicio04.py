# Ejercicio 4: calificaciones de alumnos. Calcular la calificacion promedio y la mas baja

suma = 0
calificacionBaja = 99999

# Leer 10 calificaciones
# Inicio ciclo for
for i in range(10):
    calificacion = float(input(f"Ingrese la {i + 1} calificacion: "))

    suma += calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
# Fin ciclo for

# Calculo el promedio
calificacionPromedio = suma / 10

# Mostrar resultados
print(f"La calificacion promedio es: {calificacionPromedio}")
print(f"La calificacion mas baja es: {calificacionBaja}")