#16.4 Creamos la plantilla de test_polimorfismo, método de polimorfismo
from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto) #De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto)) # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalle()) #16.5 Pruebas con otro objeto y método
    #16.6 Prueba de errores y validación con: método isinstance()
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("Pablo", 75000.00)
imprimir_detalles(empleado)

#16.5 Pruebas con otro objeto y método
gerente = Gerente('Nico', 77000.00, 'Sisemas')
imprimir_detalles(gerente)