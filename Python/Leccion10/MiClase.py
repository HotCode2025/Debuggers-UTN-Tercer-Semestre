# 13.6 Diagrama de clases UML con variables de clase: Teoría en carpeta Lección10
# 13.7 Variables de clase: Práctica en carpeta Lección10
class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):  # La variable de instancia, da diferntes valores
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():  # metodo estatico, se asocia a la clase
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

#Clase 10 POO Parte 7 Diseño, Constante y contexto estático
#14.1 Creación de variables de clase
MiClase.variable_clase2 = 'Valor de variable de Clase2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

# 14.2 Métodos estáticos
MiClase.metodo_estatico()

# 14.3 Métodos de clase
MiClase.metodo_clase()

# 14.4 Contexto estático y Dinámico
miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()