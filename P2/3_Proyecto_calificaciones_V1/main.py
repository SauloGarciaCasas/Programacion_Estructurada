"""
Proyecto 3

Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menú de opciones para agregar, mostrar y calcular promedio.
Notas:
1.- Utilizar funciones y mandar a llamar desde otro archivo (modulo).
2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, asi como las tres calificaciones.

"""
import calif

def main():
    datos = []

    opcion = True
    while opcion:
        calif.borrarPantalla()
        opcion = calif.menu_principal()

        match opcion:
            case "1":
                calif.borrarPantalla()
                calif.agregar_cal(datos)
                calif.esperetecla()
            case "2":
                calif.borrarPantalla()
                calif.mostrar_cal(datos)
                calif.esperetecla()
            case "3":
                calif.borrarPantalla()
                calif.promedio_cal(datos)
                calif.esperetecla()
            case "4":
                opcion = False
                calif.borrarPantalla()
                print("\t\t \U0001F6AA Terminaste la ejecucion del SW \U0001F6AA ")
            case _:
                calif.borrarPantalla()
                input("\t\t \u274C Opción invalida vuelva a intentarlo ... por favor \u274C ")

if __name__=="__main__":
    main()