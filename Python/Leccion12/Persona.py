# 15.6 Sobrecarga de Operadores: Parte 2a
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): # Other significa = otro
        return f'{self.nombre} {other.nombre}'

# 15.7 Sobrecarga de Operadores: Parte 2b
    def __sub__(self, other): # Sub significa = substraction (resta)
        return self.edad - other.edad

persona1 = Persona('Jairo', 35)
persona2 = Persona('Ubilla', 19)

# persona1.__add__(persona2) # Sintaxis interna y automática

print(persona1 + persona2)
print(persona1 - persona2)