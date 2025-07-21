import agenda

def main ():
    agenda_contactos = {} 
    opcion = True

    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()

        match opcion:
            case 1:
                agenda.borrarPantalla()
                agenda.agregar(agenda_contactos)
                agenda.esperar_tecla()
            case 2:
                agenda.borrarPantalla()
                agenda.mostrar(agenda_contactos)
                agenda.esperar_tecla()
            case 3:
                agenda.borrarPantalla()
                agenda.buscar(agenda_contactos)
                agenda.esperar_tecla()
            case 4:
                agenda.borrarPantalla()
                agenda.modificar(agenda_contactos)
                agenda.esperar_tecla()
            case 5:
                agenda.borrarPantalla()
                agenda.eliminar(agenda_contactos)
                agenda.esperar_tecla()
            case 6:
                agenda.borrarPantalla()
                print("Terminaste la ejecución del SW")
                opcion = False
            case _:
                agenda.borrarPantalla()
                input("Opción inválida, vuelva a intentarlo ... por favor")

main()