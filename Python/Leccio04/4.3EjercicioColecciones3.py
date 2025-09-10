# Ejercicio 3: Agregar personajes a una lista
# escriba un programa donde cree una lista con los siguientes personajes
# del señor de los anillos
"""
Nombre: ARAGORN
Clase: GUERRERO
Raza: DUNADAN DEL NORTE 

Nombre: GANDALF
Clase: MAGO
Raza: ISTAR

Nombre: LEGOLAS
Clase: ARQUERO
Raza: ELFO SINDAR 
"""
elSenorDeLosAnillos ={
        1: {"Nombre":"Aragorn","Clase":"Guerrero","Raza":"Dunadan del Norte"},
        2: {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"},
        3: {"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"},
        4: {"Nombre":"Gimli","Clase":"Guerrero","Raza":"Enano"},
}
for valor in elSenorDeLosAnillos.values():
    print(valor)
for llave, valor in elSenorDeLosAnillos.items():
    print(llave,valor)
print("Hemos cargado una lista con los personajes de El Señor de los Anillos: ")
print(len(elSenorDeLosAnillos))