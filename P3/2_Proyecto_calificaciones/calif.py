import os
import mysql.connector

def conectar():
    """Establece y devuelve una conexión y cursor a la base de datos."""
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_calificaciones"
    )
    cursor = conexion.cursor()
    return conexion, cursor

def esperetecla():
    input("\t \U0001F552 Oprima cualquier tecla para continuar ... \U0001F552")

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def menu_principal():
    print("\t \U0001F4DD .::: Sistema de Gestión de calificaciones :::... \U0001F4DD \n\t\t \U0001F4C2 1.- Agregar  \n\t\t \U0001F4C2 2.- Mostrar \n\t\t \U0001F4C2 3.- Calcular Promedio \n\t\t \U0001F4C2 4.- SALIR ")
    opcion = input("\t \u26A0 Elige una opción (1-4): ").upper()
    return opcion

def agregar_cal():
    borrarPantalla()
    print("\t \U0001F4DD Agregar Calificaciones \U0001F4DD")
    nombre = input("\t\t \U0001F464 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"\t\t \U0001F4E7 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("\t\t \u274C Ingresa un número válido (0-10) \u274C")
            except ValueError:
                print("\t\t \u274C Ingresa un valor numérico \u274C")

    conexion, cursor = conectar()
    cursor.execute("INSERT INTO alumnos (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)", (nombre, *calificaciones))
    conexion.commit()
    conexion.close()
    print("\t \u2705 Acción realizada con éxito \u2705")

def mostrar_cal():
    borrarPantalla()
    print("\t \U0001F4DD Mostrar Calificaciones \U0001F4DD")
    conexion, cursor = conectar()
    cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM alumnos")
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print(f"\U0001F50D {'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
        print(f"{'-'*45}")
        for fila in resultados:
            print(f"\U0001F50D {fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*45}")
        print(f"\U0001F50D Son {len(resultados)} alumnos")
    else:
        print("\t\t \u26A0 No hay calificaciones registradas en el sistema \u26A0")

def promedio_cal():
    borrarPantalla()
    print("\t \U0001F4DD Calcular promedio \U0001F4DD")
    conexion, cursor = conectar()
    cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM alumnos")
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print(f"\U0001F50D {'Nombre':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        total = 0
        for fila in resultados:
            promedio = round((fila[1] + fila[2] + fila[3]) / 3, 2)
            print(f"\U0001F50D {fila[0]:<15}{promedio:<10}")
            total += promedio
        grupal = round(total / len(resultados), 2)
        print(f"{'-'*30}")
        print(f"\U0001F50D El promedio grupal es: {grupal}")
        print(f"{'-'*30}")
    else:
        print("\t\t \u26A0 No hay calificaciones registradas en el sistema \u26A0")