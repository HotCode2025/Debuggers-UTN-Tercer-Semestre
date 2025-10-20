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

    def __del__(self): # Clase 10.6
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__': # Clase 10.5
    persona1 = Persona2('Jairo', 'Ubilla', 34)
    print(persona1.nombre) # Llamamos al metodo getter
    persona1.nombre = 'Wilson' # Llamamos al metodo setter
    print(persona1.nombre) # Otra vez con el metodo getter
    print(persona1.mostrar_detalles())# Llamamos al metodo mostrar detalles

    # 10.2 Atributos read-only(solo lectura)
    # Atributo read-only (solo lectura) seria la edad por que no tiene el metodo set
    print(persona1.edad)

    # 10.3 Tarea con clase persona2
    # Tarea crear tres objetos más, utilizando los metodos getter and setter
    # para modificar, y mostrar los cambios con el metodo mostrar_detalles

    persona2 = Persona2('Alex', 'Diaz', 25)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Ane'
    persona2.apellido = 'Lara'
    persona2.edad = 20
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Carol', 'Lazo', 19)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Lazio'
    persona3.edad = 20
    print(persona3.mostrar_detalles())

    persona4 = Persona2('Aleja', 'Uribe', 25)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Alexis'
    persona4.apellido = 'Rojas'
    persona4.edad = 17
    print(persona4.mostrar_detalles())
    print(__name__) # Comprobacion del modulo prinsipal en ejecucion




