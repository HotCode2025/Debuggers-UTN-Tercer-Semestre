# 15.3 Pruebas de las clases Orden y Producto
from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Remera', 120.00)
producto4 = Producto('Medias', 110.00)
producto5 = Producto('Zapatillas', 195.00)
producto6 = Producto('Campera', 295.00)
producto7 = Producto('Gorra', 157.00)

productos1 = [producto1, producto2]  # Lista de productos
productos2 = [producto3, producto4]
productos3 = [producto1, producto5]
orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto6)
orden1.agregar_producto(producto7)
print(orden1)
print(f'Total de la orden: {orden1.calcular_total()}')
orden2 = Orden(productos2)
orden2.agregar_producto(producto7)
orden2.agregar_producto(producto6)
print(orden2)
print(f'Total de la orden: {orden2.calcular_total()}')
orden3 = Orden(productos3)
print(orden3)
print(f'Total de la orden: {orden3.calcular_total()}')