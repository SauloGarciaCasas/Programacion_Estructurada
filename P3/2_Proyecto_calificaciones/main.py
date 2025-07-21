import calif

def main():
    while True:
        calif.borrarPantalla()
        opcion = calif.menu_principal()

        match opcion:
            case "1":
                calif.agregar_cal()
                calif.esperetecla()
            case "2":
                calif.mostrar_cal()
                calif.esperetecla()
            case "3":
                calif.promedio_cal()
                calif.esperetecla()
            case "4":
                calif.borrarPantalla()
                print("\t\t \U0001F6AA Terminaste la ejecucion del SW \U0001F6AA ")
                break
            case _:
                input("\t\t \u274C Opción invalida vuelva a intentarlo ... por favor \u274C ")

if __name__ == "__main__":
    main()