# Definimos una tupla
cocina = ('cuchara','cuchillo','tenedor')
print(cocina)
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papas',) # Una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de linea

# No es una buena practica
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina: Esto es para eliminar una tupla

# 2.4 Repaso y más conceptos de Tuplas
#Repaso de tuplas
tupla = (4,'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de dstos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
print(4 not in tupla)
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla
