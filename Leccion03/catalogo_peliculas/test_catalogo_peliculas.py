from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

def mostrar_menu(): #Creamos el output del programa
    print("\n--- Catálogo de Películas ---")
    print("1) Agregar películas")
    print("2) Listar películas")
    print("3) Eliminar archivo de películas")
    print("4) Salir")

while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ") #tomamos la opcion del usuario

    if opcion == "1": #para agregar peliculas
        nombre = input("Ingresá el nombre de la película: ")
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregar_pelicula(pelicula)


    elif opcion == "2": #para listarlas
        CatalogoPeliculas.listar_peliculas()

    elif opcion == "3": #para eliminar el archivo peliculas.txt
        CatalogoPeliculas.eliminar()

    elif opcion == "4": # salimos del programa
        print("Saliendo del programa...")
        break

    else: #por si el usuario ingresa una opcion invalida.
        print("Opción inválida, intentá de nuevo.")



