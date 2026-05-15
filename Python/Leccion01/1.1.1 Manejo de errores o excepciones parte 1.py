# un error o excepcion se produce cuando el programa termina de manera abrupta al encontrarse con un error.
try:
    10/0
except Exception as e:
    print(f"Ocurrió un error: {e}")
#el codigo se ejecuta igual, pero en vez de arrojar un error en el codigo, solamente indica por medio del string que existe un error, ejecutando el programa sin que aparezca en rojo.
#si el error lo ponemos antes del try, no podremos capturar la excepcion y nos dara el mismo mensaje pero como un error de codigo en consola.
try:
    10/0
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {e}")
#aqui mostramos como capturar el mismo error pero de manera mas especifica, utilizando la clase hija ZeroDivisionError, que seria la indicada para este error.