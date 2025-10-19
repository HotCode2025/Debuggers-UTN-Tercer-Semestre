# Clase 6 POO Parte 1
# 8.1 Creacion de una clase

#class Personas: # Creamos una clase
#    pass # No se procesa nada mas (No tiene contenido)
#print(type(Personas))

# 8.2 Atributos en metodos y creacion de un objeto

class Persona:
    def __init__(self, nombre, apellido, dni, edad, cuil, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.__cuil= cuil # Este atributo esta totalmente encapsulado
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalles(self): # self es igual a this en otro lenguajes
        print(f"La clase Persona tiene lo siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad} {self.__cuil}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")

persona1 = Persona("Juan", "Zalazar", 22897786, 34, 34567898762)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


# 8.3 Creacion de objetos con argumentos


persona2 = Persona('Ariel', 'Betancud', 40456234, 25, 34560984569)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

# 8.4 Creamos más objetos en una clase
persona3 = Persona('Osvaldo', 'Giordanini', 45324564, 45, 23654321234)
print(f"El objeto3 de la clase persona: {persona3.nombre} {persona3.apellido} Su edad es: {persona3.edad}")

# 8.5 Referencias de memoria de objetos con el Debug
# 8.6 Modificar atributos de un objeto

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

# 8.7 Métodos de instancia: Crear UML
# Los atributos son: Caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)

# 8.8 Métodos de instancia: Definimos un metodo

persona1.mostrar_detalles() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalles()
persona3.mostrar_detalles()

# 9.1 Palabra reservada self y atributos de instancia

# Persona.mostrar_detalles(persona1) # Debemos pasarle una referencia para el self o dará error

# 9.2 Crear atributos desde un objeto

persona1.telefono = "2604789789"
print(f"Este es el telefono de: {persona1.nombre} {persona1.telefono}")#Hemos creado un atributo de un objeto
# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error

# 9.7 Metodo init Dunder con argumentos variables
persona4 = Persona('Lisandro', 'Martinez', 27, 'Teléfono', '2604234258', 'Calle Garcia', 980, 'Manzana', 87, 'Casa', 12, Altura=175, Peso=87, CFavorito='Negro', Auto='Ford', Modelo=98)
persona4.mostrar_detalles()

# 9.8 Encapsulamiento parte 1
persona5 = Persona('Tito', 'Alaniz', 30987784, 32, 23987656754)
persona5.mostrar_detalles()
#print(persona3._dni) # esto no se debe utilizar(esta encapsulado), esto dice que desconocemos python

# 9.9 Encapsulamiento parte 2
persona6 = Persona('Pepe', 'Maza', 34234234, 21, 23654564563)
persona6.mostrar_detalles()
# persona6.__cuil # Está totalmente encapsulado