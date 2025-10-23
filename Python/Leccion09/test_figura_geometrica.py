# 12.4 Creamos la clase para testear nuestro código
from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# 12.6 Metodo MRO: Method Resolution Order
# MRO = Method Resolution Order
print(Cuadrado.mro())

# 12.8 Tarea 1 y tarea 2 Creación de la clase Rectángulo
print(cuadrado1)

print('Creacion de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'verde')
print(f'El calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#figura1 = FiguraGeometrica() #No se puede instanciar, es abstracta
print(Cuadrado.mro())