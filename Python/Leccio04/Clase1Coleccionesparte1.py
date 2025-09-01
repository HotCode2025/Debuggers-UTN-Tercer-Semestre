# lista = Ariel, Liliana, Natalia, Osvaldo
#Colecciones en Python

# Las listas el lo que se conoce en otros lenguajes como arreglos o vectores
nombres = ['Naty','Osvaldo','Lily','Ariel']

# Buscar elemento de la lista de adelante para atras
print(nombres)
print(nombres[0])
print(nombres[1])

# Buscar elemento de atras para adelante
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
#ir del inlcio de la lista al indice (Sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2

#Desde el indice indicado hasta el final
print(nombres[1: ])

# Modificamos un valor
nombres[2] = 'liliana'
nombres[0] = 'Natalia'
print(nombres)

#Iterar una lista
for nombre in nombres: #Nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron lo elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] # del significa delete(eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
#del nombres
#print(nombres) # Aqui nos mostrara un error

