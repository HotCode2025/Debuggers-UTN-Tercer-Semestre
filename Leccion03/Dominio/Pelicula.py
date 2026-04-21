class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre  # Atributo privado

    def __str__(self):
        return f"Pelicula: {self._nombre}"