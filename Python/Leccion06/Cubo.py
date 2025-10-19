# 9.6 Creamos la clase: cubo
class Cubo:
    """
    Crear la clase cubo con los atributos, ancho, alto y profundidad, con
    un meodo calcular_volumen que tedra la formula:
    volumen = ancho * altua * profundidad
    que el usuario ingrese los valores.
    """

    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = float(input("Introduce el ancho del cubo: "))
alto = float(input("Introduce el alto del cubo: "))
profundidad = float(input("Introduce la profundidad del cubo: "))

cubo1 = Cubo(ancho, alto, profundidad)
volumen = cubo1.calcular_volumen()
print("El volumen del cubo es: ", volumen)




