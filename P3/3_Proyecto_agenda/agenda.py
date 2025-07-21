import mysql.connector
from mysql.connector import Error

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_agenda"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("Oprima ENTER para continuar: ")

def obtener_1_a_6(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if 0 < valor < 7:
                return valor
            else:
                print("Por favor ingrese un valor del 1 al 6 \u2328\uFE0F")
        except ValueError:
            print("Por favor ingrese un número entero (1-6) \u2328\uFE0F")

def menu_principal():
    print(f"{' '*12}\U0001F4BB ..::: Sistema de gestión de contactos :::.. \U0001F4BB\n")
    print(f"{' '*30}1️⃣  Agregar Contacto")
    print(f"{' '*30}2️⃣  Mostrar Contactos")
    print(f"{' '*30}3️⃣  Buscar Contactos")
    print(f"{' '*30}4️⃣  Modificar Contactos")
    print(f"{' '*30}5️⃣  Eliminar Contactos")
    print(f"{' '*30}6️⃣  Salir\n")
    return obtener_1_a_6("\t\t👉 Elige una opción (1-6): ")

def agregar(_):
    print("\t\t\\.:: Agregar Contacto ::.")
    nombre = input("Nombre del contacto: ").upper().strip()
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
    if cursor.fetchone():
        print("\n\t\t\u26A0\uFE0F El contacto ya existe \u26A0\uFE0F")
    else:
        telefono = input("Teléfono: ").strip()
        email = input("E-mail: ").lower().strip()
        cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)",
                       (nombre, telefono, email))
        conn.commit()
        print("\n\t\t\u2705 Contacto agregado exitosamente")
    cursor.close()
    conn.close()

def mostrar(_):
    print("\t\t\\.:: Mostrar Contactos ::.")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    resultados = cursor.fetchall()
    if not resultados:
        print("\n\t\t\u26A0\uFE0F No existen contactos en la agenda \u26A0\uFE0F")
    else:
        for nombre, telefono, email in resultados:
            print(f"\n\tNombre: {nombre}\n\tTeléfono: {telefono}\n\tE-mail: {email}")
    cursor.close()
    conn.close()

def buscar(_):
    print("\t\t\\.:: Buscar Contacto ::.")
    nombre = input("Nombre del contacto a buscar: ").upper().strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"\n\tNombre: {resultado[0]}\n\tTeléfono: {resultado[1]}\n\tE-mail: {resultado[2]}")
    else:
        print("\n\t\t\u26A0\uFE0F Contacto no encontrado \u26A0\uFE0F")
    cursor.close()
    conn.close()

def modificar(_):
    print("\t\t\\.:: Modificar Contacto ::.")
    nombre = input("Nombre del contacto a modificar: ").upper().strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"\n\tContacto actual:\n\tTeléfono: {resultado[1]}\n\tE-mail: {resultado[2]}")
        nuevo_telefono = input("Nuevo teléfono (dejar en blanco para mantener actual): ").strip()
        nuevo_email = input("Nuevo e-mail (dejar en blanco para mantener actual): ").strip()

        if nuevo_telefono == "":
            nuevo_telefono = resultado[1]
        if nuevo_email == "":
            nuevo_email = resultado[2]

        cursor.execute("UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s",
                       (nuevo_telefono, nuevo_email, nombre))
        conn.commit()
        print("\n\t\t\u2705 Contacto modificado exitosamente")
    else:
        print("\n\t\t\u26A0\uFE0F Contacto no encontrado \u26A0\uFE0F")
    cursor.close()
    conn.close()

def eliminar(_):
    print("\t\t\\.:: Eliminar Contacto ::.")
    nombre = input("Nombre del contacto a eliminar: ").upper().strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
    if cursor.fetchone():
        confirmar = input(f"¿Estás seguro que deseas eliminar a {nombre}? (s/n): ").lower()
        if confirmar == 's':
            cursor.execute("DELETE FROM contactos WHERE nombre = %s", (nombre,))
            conn.commit()
            print("\n\t\t\u2705 Contacto eliminado exitosamente")
        else:
            print("\n\t\t\u274C Operación cancelada")
    else:
        print("\n\t\t\u26A0\uFE0F Contacto no encontrado \u26A0\uFE0F")
    cursor.close()
    conn.close()