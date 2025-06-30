def esperetecla():
    input("\t \U0001F552 Oprima cualquier tecla para continuar ... \U0001F552")

def borrarPantalla():
    import os
    os.system("cls")

def menu_principal():
    print("\t \U0001F4DD .::: Sistema de Gestión de calificaciones :::... \U0001F4DD \n\t\t \U0001F4C2 1.- Agregar  \n\t\t \U0001F4C2 2.- Mostrar \n\t\t \U0001F4C2 3.- Calcular Promedio \n\t\t \U0001F4C2 4.- SALIR ")
    opcion = input("\t \u26A0 Elige una opción (1-4): ").upper()
    return opcion

def agregar_cal(lista):
    borrarPantalla()
    print("\t \U0001F4DD Agregar Calificaciones \U0001F4DD")
    nombre = input("\t\t \U0001F464 Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua = True
        while continua:
            try:
                cal = float(input(f"\t\t \U0001F4E7 Calificación {i}: "))
                if cal >= 0 and cal < 11:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("\t\t \u274C Ingresa un número válido \u274C")
            except ValueError:
                print("\t\t \u274C Ingresa un valor numérico \u274C")
    lista.append([nombre] + calificaciones)
    print("\t \u2705 Acción realizada con éxito \u2705")

def mostrar_cal(lista):
    borrarPantalla
    print("\t \U0001F4DD Mostrar Calificaciones \U0001F4DD")
    if len(lista) > 0:
        print(f"\U0001F50D {'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
        print(f"{'-'*45}")
        for fila in lista:
            print(f"\U0001F50D {fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*45}")
        cuantos=len(lista)
        print(f"\U0001F50D Son {cuantos} alumnos")
    else:
        print("\t\t \u26A0 No hay calificaciones registradas en el sistema \u26A0")

def promedio_cal(lista):
    borrarPantalla()
    print("\t \U0001F4DD Calcular promedio \U0001F4DD")
    if len(lista) > 0:
        print(f"\U0001F50D {'Nombre':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            promedio = round((fila[1] + fila[2] + fila[3]) / 3, 2)
            print(f"\U0001F50D {fila[0]:<15}{promedio:<10}")
            promedio_grupal+=promedio
        print(f"{'-'*30}")
        promedio_grupal=round(promedio_grupal/len(lista), 2)
        print(f"\U0001F50D El promedio grupal es: {promedio_grupal}")
        print(f"{'-'*30}")
    else:
        print("\t\t \u26A0 No hay calificaciones registradas en el sistema \u26A0")