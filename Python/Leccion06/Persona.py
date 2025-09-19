# 8.1 Creacion de una clase

#class Personas: # Creamos una clase
#    pass # No se procesa nada mas (No tiene contenido)
#print(type(Personas))

# 8.2 Atributos en metodos y creacion de un objeto

class Persona:
    def __init__(self, nombre, apellido, edad): # Se lo llama metodo Init Dunder
        self.nombre = 'Juan'
        self.apellido = 'Zalazar'
        self.edad = 22
    def mostrar_detalles(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1 = Persona("Juan", "Zalazar", 22)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


# 8.3 Creacion de objetos con argumentos


persona2 = Persona('Ariel', 'Betancud', 40)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

# 8.4 Creamos mas objetos en una clase
persona3 = Persona('Osvaldo', 'Giordanini', 45)
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

persona1.mostrar_detalles()
persona2.mostrar_detalles()