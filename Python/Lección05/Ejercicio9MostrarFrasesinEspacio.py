# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase pero sin espacios en blanco,
# además un contador de cuántos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:       Frase = vivir por siempre en paz
#                Frase Final = vivirporsiempreenpaz
#                N° de caracteres = 20

# Frase sin espacios
frase = input("Introduce una frase: ")

frase_sin_espacios = " "

for caracter in frase:
    if caracter != " ":
        frase_sin_espacios += caracter

print("Frase sin espacios:", frase_sin_espacios)
print("Número de caracteres de la frase: ", len(frase_sin_espacios))