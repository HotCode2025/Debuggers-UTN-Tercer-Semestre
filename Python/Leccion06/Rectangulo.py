# 9.5 Creamos la clase: Rectángulo
class Rectangulo:
    """
    Crear una clase llamada Rectángulo, debe tenér 2 atributos: altura y base
    el nombre del metodo será calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = float(input("Digite el valor de la base: "))
altura = float(input("Digite el valor de la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")