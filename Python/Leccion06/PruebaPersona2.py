# Clase 08
# 10.4 Uso de clases y módulos

from Persona2 import Persona2
print('Creación de objetos'.center(50, '-')) # Clase 10.6
if __name__ == '__main__': # Clase 10.5
    persona5 = Persona2('Anibal', 'Fernandez', 35)
    persona5.mostrar_detalles()

# 10.5 Comprobación del módulo principal en ejecución
    print(__name__) # Comprobacion del modulo prinsipal en ejecucion
print('Eliminación de objetos'.center(50, '-')) # Clase 10.6

# Clase 10.6 Destructor de objetos
del persona5


