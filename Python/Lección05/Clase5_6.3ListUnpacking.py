# 6.3 List Unpacking: Desempaquetado de listas
# Desempaquetado de listas o list Unpacking

def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto

person2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*person2)

person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

# 6.4 Repaso del Ciclo for else

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

# 6.5 List Comprehension, Lista de Comprension

names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueve lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mex"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b ["country"] == "Arg"]
print(Arg)
print(bottleC)

# 6.6 Funciones, Paso de Argumentos (funciones)

def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a traves del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

# 6.7 Funciones, Palabra return
# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

# 6.8 Funciones, Valores por Default en Argumentos

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado2 = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# 6.9 Funciones, Argumentos, Variables en Funciones

def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')




