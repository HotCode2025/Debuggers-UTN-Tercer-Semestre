
# Ejercicio 4: Etapas de Vida
# Haremos un programa que cuando el usuario ingrese
# su edad le diga o imprima la etapa de su vida en una breve oracion:

edad = input("Ingrese su edad: ") or None
if edad is not None:
    edad = int(edad)
    if 0 <= edad <= 9:
        print("La infancia es increible y bella")
    elif 10 <= edad <= 19:
        print("Tienes muchos cambios, mucho que estudiar")
    elif 20 <= edad <= 29:
        print("Amor y comienza el trabajo")
    elif 30 <= edad <= 39:
        print("La familia se agranda")
    elif 40 <= edad <= 49:
        print("La plenitud de la vida")
    elif 50 <= edad <= 59:
        print("Me cruje la rodilla")
    elif 60 <= edad <= 69:
        print("Llegan los nietos")
    elif 70 <= edad <= 79:
        print("Descanso y viajes")
    elif 80 <= edad <= 89:
        print("Mas olor a cajon que a fruta")
    else:
        print("Cuanto mas queres vivir?")
else:
    print("Error: Debe ingresar su edad")