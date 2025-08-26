# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorre los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una funcion para recorrrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # Devuelve un booleano
print('IDE' not in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # El diccionario se borro


# 2.3 Repaso y más conceptos de listas

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # Esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento, en python es una funcion
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)


# 2.4 Repaso y más conceptos de Tuplas
#Repaso de tuplas
tupla = (4,'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de dstos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
print(4 not in tupla)
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

























