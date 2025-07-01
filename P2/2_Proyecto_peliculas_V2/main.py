"""
Crear un proyecto que permita gestionar (administrar) películas, colocar un menú de opciones para agregar, eliminar, modificar
y consultar películas.
Notas:
1.- Utilizar funciones y mandar a llamar desde otro archivo.
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoría, clasificación. genero, idioma).

"""
import peliculas

while True:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Crear  \n 2.- Borrar \n 3.- Mostrar \n 4.- Agregar Característica \n 5.- Modificar Característica \n 6.- Borrar Característica \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.borrarPantalla()
            peliculas.crear()
        case "2":
            peliculas.borrarPantalla()
            peliculas.borrar()
        case "3":
            peliculas.borrarPantalla()
            peliculas.mostrar()
        case "4":
            peliculas.borrarPantalla()
            peliculas.agregarcar()
        case "5":
            peliculas.borrarPantalla()
            peliculas.modificarcar()
        case "6":
            peliculas.borrarPantalla()
            peliculas.borrarcar()
        case "7":
            peliculas.borrarPantalla()
            print("Terminaste la ejecucion del SW")
            break
        case _:
            peliculas.borrarPantalla()
            input("Opción invalida vuelva a intentarlo ... por favor")