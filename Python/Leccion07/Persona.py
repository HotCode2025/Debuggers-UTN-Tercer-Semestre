# 11.3 Herencia, ahora en la práctica: deben hacer tarea
class Persona:  #Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad


    @property
    def nombre(self):  # Metodo Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        self._nombre = nombre

    @property  # Decorador
    def edad(self):  # Metodo Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Metodo Setter
        self._edad = edad

    def __str__(self):
        return f'Persona: [ Nombre: {self._nombre}, Edad: {self._edad} ]'

# Clase empleado

class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def mostrar_detalles(self): # Override = sobreescribir
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._edad} {self._sueldo}')


    @property
    def sueldo(self):  # Metodo Getter
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):  # Metodo Setter
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}'


empleado1 = Empleado('Nico', 27, 65000)
print(empleado1.nombre)
empleado1.nombre = 'Nicolas'
print(empleado1.edad)
empleado1.edad = 30
print(empleado1.sueldo)
empleado1.sueldo = 69000
print(empleado1.mostrar_detalles())

# Tarea: encapsular los atributos y agregar los métodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Fabi', 23, 45000)
print(empleado2.nombre)
empleado2.nombre = 'Fabian'
print(empleado2.edad)
empleado2.edad = 25
print(empleado2.sueldo)
empleado1.sueldo = 50000
print(empleado2.mostrar_detalles())
