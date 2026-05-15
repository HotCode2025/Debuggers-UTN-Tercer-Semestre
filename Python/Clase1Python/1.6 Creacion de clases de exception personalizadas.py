# 1.6 Creación de clases de Exception personalizadas
# Creando una exception personalizada
class NumerosIgualesExcepion (Exception): # Extiende de la clase
    def __init__(self, mensaje):
        self.message = mensaje