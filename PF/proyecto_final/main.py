from Modelos import usuario as musuario
import alumnos
import getpass

def menu_login():
    alumnos.limpiar_pantalla()
    print("\n\U0001F511  Autenticación\n" + "─"*60)
    print("1\U0000FE0F\u20E3  Iniciar sesión")
    print("2\U0000FE0F\u20E3  Registrarme")
    print("3\U0000FE0F\u20E3  Salir")
    while True:
        try:
            op = int(input("\U0001F449  Elige una opción (1-3): "))
            if 1 <= op <= 3:
                return op
            print("\U000026A0\U0000FE0F  Opción inválida.")
            alumnos.esperar_tecla()
        except ValueError:
            print("\U000026A0\U0000FE0F  Ingresa un número 1-3.")
            alumnos.esperar_tecla()

def flujo_login():
    while True:
        opcion = menu_login()
        if opcion == 1:
            alumnos.limpiar_pantalla()
            email = input("Correo: ").strip()
            pwd   = getpass.getpass("Contraseña: ")
            user = musuario.login(email, pwd)
            if user:
                print(f"\U00002705  Bienvenido, {user['nombre']}.")
                return user
            else:
                print("\U0000274C  Credenciales inválidas.")
        elif opcion == 2:
            alumnos.limpiar_pantalla()
            nombre = input("Nombre: ").strip()
            email  = input("Correo: ").strip()
            pwd    = getpass.getpass("Contraseña: ")
            uid = musuario.registrar(nombre, email, pwd)
            if uid:
                print("\U00002705  Usuario registrado. Ahora inicia sesión.")
            else:
                print("\U0000274C  Ese correo ya está registrado.")
        else:
            return None

def menu_grupos(user):
    opcion = True
    while opcion:
        alumnos.limpiar_pantalla()
        opcion = alumnos.menu_principal()

        match opcion:
            case 1:
                alumnos.limpiar_pantalla()
                alumnos.agregar_grupos(user)
            case 2:
                alumnos.limpiar_pantalla()
                alumnos.mostrar(user)
                alumnos.esperar_tecla()
            case 3:
                alumnos.limpiar_pantalla()
                alumnos.modificar(user)
                alumnos.esperar_tecla()
            case 4:
                alumnos.limpiar_pantalla()
                alumnos.eliminar_grupos(user)
                alumnos.esperar_tecla()
            case 5:
                alumnos.limpiar_pantalla()
                alumnos.buscar_grupos(user)
                alumnos.esperar_tecla()
            case 6:
                alumnos.limpiar_pantalla()
                print("\U000026A0\U0000FE0F  Esta acción borrará TODOS tus grupos y alumnos.")
                if input("¿Deseas continuar? (SI/NO): ").strip().upper() == "SI":
                    from Modelos import grupo as mgrupo
                    for g in mgrupo.listar(user["id"]):
                        mgrupo.eliminar(g["id"], user["id"])
                    print("\U0001F5D1\U0000FE0F  Datos eliminados.")
                alumnos.esperar_tecla()
            case 7:
                alumnos.limpiar_pantalla()
                from Modelos import grupo as mgrupo
                if mgrupo.listar(user["id"]):
                    if input("¿Deseas exportar tus datos antes de salir? (SI/NO): ").strip().upper() == "SI":
                        alumnos.exportar_datos(user)
                print("Has cerrado sesión.")
                return  # <-- en vez de cerrar el programa, regresamos al login
            case _:
                alumnos.limpiar_pantalla()
                input("Opción inválida, vuelva a intentarlo ... por favor")

def main():
    while True:
        user = flujo_login()
        if not user:
            print("Fin de la ejecución del SW")
            break
        menu_grupos(user)

if __name__ == "__main__":
    main()
