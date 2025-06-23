# Ejercicio 3 : Calcular estacion del año
# Pedir al usuario que ingrese un mes del año, el valor
# debe ser entre 1 y 12, luego decimos en que estacion de ao esta.

mes = int(input("Ingresa un numero del mes (1 al 12): "))
if mes is None:
    print("No se ingreso ningun mes")
else:
    if 1 <= mes <= 12:
        if mes in [1,2,3]:
            print("La estacion es Verano")
        elif mes in [4,5,6]:
            print("La estacion es Otoño")
        elif mes in [7,8,9]:
            print("La estacion es Invierno")
        else:
            print("La estacion es Primavera")
    else:
        print("El numero debe ser entre 1 y 12")