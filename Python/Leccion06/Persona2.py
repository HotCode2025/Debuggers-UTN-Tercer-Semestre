# Clase 8
# 10.1 Métodos: setter and getter parte 1 y 2
class Persona2:
    def __init__(self, nombre, apellido, edad): # Está encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property # Decorador
    def nombre(self): # Metodo Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # Metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):  # Metodo Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter
        self._apellido = apellido

    @property  # Decorador
    def edad(self):  # Metodo Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Metodo Setter
       self._edad = edad

persona1 = Persona2('Jairo', 'Ubilla', 34)
print(persona1.nombre) # Llamamos al metodo getter
persona1.nombre = 'Wilson' # Llamamos al metodo setter
print(persona1.nombre) # Otra vez con el metodo getter
print(persona1.mostrar_detalles())# Llamamos al metodo mostrar detalles

# 10.2 Atributos read-only(solo lectura)
# Atributo read-only (solo lectura) seria la edad por que no tiene el metodo set
print(persona1.edad)