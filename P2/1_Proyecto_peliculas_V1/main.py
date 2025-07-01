"""
Crear un proyecto que permita gestionar (administrar) películas, colocar un menú de opciones para agregar, eliminar, modificar
y consultar películas.
Notas:
1.- Utilizar funciones y mandar a llamar desde otro archivo.
2.- Utilizar listas para almacenar nombres de películas.

"""
import peliculas

while True:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.borrarPantalla()
            peliculas.agregar()
        case "2":
            peliculas.borrarPantalla()
            peliculas.eliminar()
        case "3":
            peliculas.borrarPantalla()
            peliculas.actualizar()
        case "4":
            peliculas.borrarPantalla()
            print(".:: Consultar Peliculas ::.")
            for p in peliculas.consultar():
                print(f"- {p}")
            input("Oprima cualquier tecla para continuar ...")
        case "5":
            peliculas.borrarPantalla()
            nombre = input("Nombre de la película a buscar: ")
            if peliculas.buscar(nombre):
                print("La película SÍ está en la lista.")
            else:
                print("La película NO está en la lista.")
            input("Oprima cualquier tecla para continuar ...")
        case "6":
            peliculas.borrarPantalla()
            peliculas.vaciar()
            print("Lista de películas vaciada.")
            input("Oprima cualquier tecla para continuar ...")
        case "7":
            peliculas.borrarPantalla()
            print("Terminaste la ejecucion del SW")
            break
        case _:
            peliculas.borrarPantalla()
            input("Opción invalida vuelva a intentarlo ... por favor")