from NumerosIgualesException import NumerosIgualesExcepion # Importamos la excepción personalizada
# Clase 1 Excepciones
# 1.1 Manejo de errores o excepciones Parte 1 y 2
try:
    10/2
except Exception as e:
    print(f'Ocurrió un error: {e}')

# 1.2 Procesamiento de excepciones
# Exception con variables globales
resultado = None
a = 11
b = 0
try:
    resultado = a / b
except Exception as er:
    print(f'Ocurrió un error: {er}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# 1.3 Procesar clases de exception más específicas
resultado = None
c = 7
d = 0
try:
    resultado = c / d
except TypeError as err:
    print(f'TypeError - Ocurrió un error: {type(err)}')
except ZeroDivisionError as err:
    print(f'ZeroDivisionError - Ocurrió un error: {type(err)}')
except Exception as err:
    print(f'Exception - Ocurrió un error: {type(err)}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# 1.4 Más de procedimientos de excepciones
# Exception con variables detro del bloque try
# Pidiendo datos al usuario
resultado = None
try:
    e = int(input('Digite el primer número: '))
    f = int(input('Digite el segundo número: '))
    resultado = e / f
except TypeError as err:
    print(f'TypeError - Ocurrió un error: {type(err)}')
except ZeroDivisionError as err:
    print(f'ZeroDivisionError - Ocurrió un error: {type(err)}')
except Exception as err:
    print(f'Exception - Ocurrió un error: {type(err)}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# 1.5 Bloques else y finally al manejar excepciones
# Else se usa para cuando no hay ninguna excepción
# Finally se usa para finalizar y avisar que termino el manejo de excepciones
resultado = None
try:
    e = int(input('Digite el primer número: '))
    f = int(input('Digite el segundo número: '))
    if e == f:  # Agregamos la excepción personalizada
        raise NumerosIgualesExcepion('Son números iguales')
    resultado = e / f
except TypeError as err:
    print(f'TypeError - Ocurrió un error: {type(err)}')
except ZeroDivisionError as err:
    print(f'ZeroDivisionError - Ocurrió un error: {type(err)}')
except Exception as err:
    print(f'Exception - Ocurrió un error: {type(err)}')
else:
    print('No se arrojo ninguna excepción')
finally:
    print('Ejecución del bloque finally')

print(f'El resultado es: {resultado}')
print('seguimos...')


