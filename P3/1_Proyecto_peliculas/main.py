"""
Crear un proyecto que permita gestionar (administrar) películas, colocar un menú de opciones para agregar, eliminar, modificar
y consultar películas.
Notas:
1.- Utilizar funciones y mandar a llamar desde otro archivo.
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoría, clasificación. genero, idioma).
3.- Utilizar e implementar una base de datos para gestionar peliculas

"""
import peliculas

while True:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Crear  \n 2.- Borrar \n 3.- Mostrar \n 4.- Modificar \n 5.- Buscar \n 6.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarPantalla()
            print("Terminaste la ejecucion del SW")
            break
        case _:
            peliculas.borrarPantalla()
            input("Opción invalida vuelva a intentarlo ... por favor")