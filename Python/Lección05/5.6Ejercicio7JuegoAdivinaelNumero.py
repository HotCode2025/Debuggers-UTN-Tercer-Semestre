# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el número de intentos.

import random


def adivina_numero():

    # Generamos el número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    intentos = 0
    adivinado = False

    print("Bienvenido al juego Adivina el Número")
    print("He pensado un número entre el 1 y el 100... ¿Podrás Adivinarlo?")

    while not adivinado:
        # Pedimos el número al usuario
        try:
            intento = int(input("Ingresa un número: "))
            intentos += 1
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        # Comparamos el intento con el número secreto
        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Correcto! El número era {numero_secreto}.")
            print(f"Lo lograste en {intentos} intentos.")
            adivinado = True


# Llamamos a la funcion para jugar
adivina_numero()
