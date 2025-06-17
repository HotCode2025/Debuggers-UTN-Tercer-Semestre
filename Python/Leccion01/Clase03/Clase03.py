#Clase 3 _ 3.1 Tipos de datos
#Tipos int,float,String,Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

#Manejos de cadenas (String)
miGrupoFavorito = "The Letter Black :"
Caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es: ", miGrupoFavorito,Caracteristicas)

numero1 = "7"
numero2 = "8"
print(numero1+numero2)
print(int(numero1) + int(numero2))

#Tipos boleanos (Boot)
miBoleano = 1 > 2
print(miBoleano)

miBoleano1 = 3 > 2
print(miBoleano1)

if miBoleano:
    print("El resultado es falso")
else:
    print("El resultado es verdadero")

if miBoleano1:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# Funcion imput
resultado = input("Digite un numero: ") # Reresa un dato tipo String
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numer: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# Ejercicio "Como estuvo tu dia"
nombre = input("Cual es tu nombre: ")
print("Buenos dias", nombre)
respuesta = input("Como estuvo tu dia(1 al 10): ")
print("Mi dia estuvo: ", respuesta)

# Ejercicio Nombre del libro y autor
titulo = input("Ingrese el titulo del libro: ")
autor = input("Ingrese el nombre del autor: ")
print(titulo, "fue escrito por",autor)