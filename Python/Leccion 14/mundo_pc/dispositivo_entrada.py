#17.3 Creamos la clase padre: DispositivoEntrada
class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada