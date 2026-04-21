import os #lo usamos para crear la conexion con el sistema operativo

class CatalogoPeliculas: # Creamos la clase
    ruta_archivo = "peliculas.txt" #generamos el string para el nombre del archivo

    @staticmethod #creamos el metodo para agregar peliculas
    def agregar_pelicula (pelicula):
        with open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula._nombre}\n')
            print(f"La película {pelicula._nombre} se agregó correctamente.")

    @staticmethod #creamos el metodo para poder listar y ver las peliculas agregadas
    def listar_peliculas():
        try:
            with open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf8') as archivo:
                print('Catálogo de Películas'.center(30, '-'))
                print(archivo.read())
        except FileNotFoundError:
            print("No hay peliculas para listar, el catálogo está vacío.")

    @staticmethod #creamos el metodo para eliminar el archivo .txt
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print(f"Archivo {CatalogoPeliculas.ruta_archivo} eliminado.")
        except FileNotFoundError:
            print("El archivo de películas no existe")
