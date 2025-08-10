import alumnos

def main():
    datos = []  # compatibilidad con firmas existentes
    opcion = True

    while opcion:
        alumnos.limpiar_pantalla()
        opcion = alumnos.menu_principal()

        match opcion:
            case 1:
                alumnos.limpiar_pantalla()
                alumnos.agregar_grupos(datos)
            case 2:
                alumnos.limpiar_pantalla()
                alumnos.mostrar(datos)
                alumnos.esperar_tecla()
            case 3:
                alumnos.limpiar_pantalla()
                alumnos.modificar(datos)
                alumnos.esperar_tecla()
            case 4:
                alumnos.limpiar_pantalla()
                alumnos.eliminar_grupos(datos)
                alumnos.esperar_tecla()
            case 5:
                alumnos.limpiar_pantalla()
                alumnos.buscar_grupos(datos)
                alumnos.esperar_tecla()
            case 6:
                alumnos.limpiar_pantalla()
                alumnos.vaciar_grupos(datos)
                alumnos.esperar_tecla()
            case 7:
                alumnos.limpiar_pantalla()
                print("Terminaste la ejecución del SW")
                opcion = False
            case _:
                alumnos.limpiar_pantalla()
                input("Opción inválida, vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()