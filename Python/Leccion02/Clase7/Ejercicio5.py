# Ejerscicio 5: Sistema de calificaciones
# El objetivo del programa será crear un sistema de
# calificacionesde la siguiente manera:

calificacion = input("Ingrese la calificacion(0 a 10): ") or None
if calificacion is not None:
    calificacion = float(calificacion)
    if 0 <= calificacion <= 10:
        if 9 <= calificacion <= 10:
            print("La calificacion es A")
        elif 8 <= calificacion < 9:
            print("La calificacion es B")
        elif 7 <= calificacion < 8:
            print("La calificacion es C")
        elif 6 <= calificacion < 7:
            print("La calificacion es D")
        else:
            print("La calificacion es F")
    else:
        print("Error: El numero debe ser entre 1 y 10")
else:
    print("Error: Debe ingresar un numero")