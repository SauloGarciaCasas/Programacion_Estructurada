import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado = usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print(f"\n\t{nombre} {apellidos} se registro correctamente con el email: {email}")
            else:
                print("\n\t ...Por favor intentelo de nuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            #menu_notas(19,"Dago","Fiscal")
            registro = usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0], registro[1], registro[2])
            else:
                print(f"\n\t E-Mail y/o contraseña incorrectas, vuelve a intentarlo ...")
                funciones.esperarTecla()
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta = nota.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print(f"Se creo la nota: {titulo} exitosamente")
            else:
                print(f"No fue posible crear la nota en este momento, vuelve a intentar ...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las Notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                print(f"-"*80) 
            else:
                print(f"\n \t No existen notas para buscar") 
            funciones.esperarTecla()
        elif opcion == '3' or opcion == "CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, estas son tus notas actuales ::. \n")
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<25}{'Fecha':<20}")
                print("-" * 70)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<25}{fila[4]}")
                print("-" * 70)
                decision = input("\n¿Deseas cambiar alguna nota? (s/n): ").strip().lower()
                if decision == 's':
                    try:
                        id = int(input("\tID de la nota a actualizar: ").strip())
                        titulo = input("\tNuevo título: ").strip()
                        descripcion = input("\tNueva descripción: ").strip()
                        respuesta = nota.cambiar(id, titulo, descripcion)
                        if respuesta:
                            print(f"\n La nota {id} fue actualizada exitosamente.")
                        else:
                            print(f"\nNo se pudo actualizar la nota. Verifica el ID e intenta nuevamente.")
                    except ValueError:
                        print("\nEl ID debe ser un número entero.")
                else:
                    print("\nNo se realizará ningún cambio.")
            else:
                print("\nNo tienes notas registradas.")
            funciones.esperarTecla()     
        elif opcion == '4' or opcion == "ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, estas son tus notas actuales ::. \n")
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<25}{'Fecha':<20}")
                print("-" * 70)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<25}{fila[4]}")
                print("-" * 70)
                decision = input("\n¿Deseas eliminar alguna nota? (s/n): ").strip().lower()
                if decision == 's':
                    try:
                        id = int(input("\tID de la nota a eliminar: ").strip())
                        respuesta = nota.borrar(id)
                        if respuesta:
                            print(f"\nLa nota {id} fue eliminada exitosamente.")
                        else:
                            print(f"\nNo se pudo eliminar la nota. Verifica el ID e intenta nuevamente.")
                    except ValueError:
                        print("\nEl ID debe ser un número entero.")
                else:
                    print("\nNo se eliminará ninguna nota.")
            else:
                print("\nNo tienes notas registradas.")
            funciones.esperarTecla()
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


