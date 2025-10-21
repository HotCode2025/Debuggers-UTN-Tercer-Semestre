# 12.4 Creamos la clase para testear nuestro código
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# 12.6 Metodo MRO: Method Resolution Order
# MRO = Method Resolution Order
print(Cuadrado.mro())

# 12.8 Tarea 1 y tarea 2 Creación de la clase Rectángulo
print(cuadrado1)

rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'El calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)


