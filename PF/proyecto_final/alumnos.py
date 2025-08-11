import os
from Modelos import grupo as mgrupo, alumno as malumno
from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

SEP = "─" * 60

# ---------- Utilidades ----------
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("\n\U000023CE  Oprima ENTER para continuar... ")

def obtener_1_a_7(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if 1 <= valor <= 7:
                return valor
            print("\U000026A0\U0000FE0F  Ingrese un valor del 1 al 7.")
        except ValueError:
            print("\U000026A0\U0000FE0F  Ingrese un número entero (1-7).")

def obtener_SI_NO(mensaje):
    while True:
        valor = input(mensaje).strip().upper()
        if valor in ("SI", "NO"):
            return valor
        print('\U000026A0\U0000FE0F  Responda con "SI" o "NO".')

# ---------- Menú ----------
def menu_principal():
    print("\n\U0001F4BB  Sistema de gestión de grupos y alumnos\n" + SEP)
    print("1\U0000FE0F\u20E3  Agregar")
    print("2\U0000FE0F\u20E3  Mostrar")
    print("3\U0000FE0F\u20E3  Modificar")
    print("4\U0000FE0F\u20E3  Eliminar")
    print("5\U0000FE0F\u20E3  Buscar")
    print("6\U0000FE0F\u20E3  Vaciar")
    print("7\U0000FE0F\u20E3  Salir")
    print(SEP)
    return obtener_1_a_7("\U0001F449  Elige una opción (1-7): ")

# ---------- Agregar ----------
def agregar_grupos(_unused):
    print("\n\U0001F4DA  Agregar grupos\n" + SEP)
    respuesta_grupo = "SI"

    while respuesta_grupo == "SI":
        nombre_grupo = input("\U0001F4DD  Nombre del grupo a añadir: ").strip()
        if not nombre_grupo:
            print("\U000026A0\U0000FE0F  El nombre del grupo no puede estar vacío.")
            continue

        existente = mgrupo.obtener_por_nombre(nombre_grupo)
        if existente:
            print(f"\U00002139\U0000FE0F  El grupo «{nombre_grupo}» ya existe.")
            id_grupo = existente["id"]
        else:
            id_grupo = mgrupo.crear(nombre_grupo)
            print(f"\U00002705  Grupo «{nombre_grupo}» creado.")

        # alumnos del grupo
        while obtener_SI_NO("¿Agregar un alumno? (SI/NO): ") == "SI":
            nombre_alumno = input("\U0001F464  Nombre del alumno: ").strip()
            if nombre_alumno:
                malumno.crear(nombre_alumno, id_grupo)
                print(f"\U00002795  Alumno «{nombre_alumno}» agregado.")
            else:
                print("\U000026A0\U0000FE0F  Nombre vacío, se omite.")

        respuesta_grupo = obtener_SI_NO("¿Añadir otro grupo? (SI/NO): ")

# ---------- Mostrar (solo nombres, sin id ni fecha) ----------
def mostrar(_unused):
    print("\n\U0001F4C2  Mostrar grupos y alumnos\n" + SEP)
    grupos = mgrupo.listar()
    if not grupos:
        print("\u25FE  No hay grupos registrados.")
        return

    for g in grupos:
        print(SEP)
        print(f"\U0001F4C1  Grupo: {g['nombre']}")
        alumnos = malumno.listar_por_grupo(g["id"])
        if alumnos:
            print("\U0001F465  Alumnos:")
            for a in alumnos:
                print(f"   • {a['nombre']}")
        else:
            print("\U0001F6C7  (Sin alumnos)")
    print(SEP)

# ---------- Eliminar ----------
def eliminar_grupos(_unused):
    print("\n\U0001F5D1\U0000FE0F  Eliminar\n" + SEP)
    print("1) Eliminar grupo completo")
    print("2) Eliminar alumno de un grupo")
    opcion = input("\U0001F449  Elige una opción (1 o 2): ").strip()

    if opcion == "1":
        nombre_grupo = input("\U0001F4C1  Nombre del grupo a eliminar: ").strip()
        g = mgrupo.obtener_por_nombre(nombre_grupo)
        if not g:
            print("\U0000274C  Grupo no encontrado.")
            return
        if obtener_SI_NO("¿Eliminar este grupo y sus alumnos? (SI/NO): ") == "SI":
            ok = mgrupo.eliminar(g["id"])
            print("\U0001F5D1\U0000FE0F  Grupo eliminado." if ok else "\U0000274C  No se pudo eliminar.")
        else:
            print("\u21A9\U0000FE0F  Operación cancelada.")

    elif opcion == "2":
        nombre_grupo = input("\U0001F4C1  Grupo: ").strip()
        g = mgrupo.obtener_por_nombre(nombre_grupo)
        if not g:
            print("\U0000274C  Grupo no encontrado.")
            return
        nombre_alumno = input("\U0001F464  Alumno a eliminar: ").strip()
        resultados = malumno.buscar_por_nombre(nombre_alumno)
        candidatos = [a for a in resultados if a["grupo_id"] == g["id"]]
        if not candidatos:
            print("\U0000274C  Alumno no encontrado en ese grupo.")
            return
        a = candidatos[0]
        if obtener_SI_NO(f"¿Eliminar a «{a['nombre']}»? (SI/NO): ") == "SI":
            ok = malumno.eliminar(a["id"], grupo_id=g["id"])
            print("\U0001F5D1\U0000FE0F  Alumno eliminado." if ok else "\U0000274C  No se pudo eliminar.")
        else:
            print("\u21A9\U0000FE0F  Operación cancelada.")
    else:
        print("\U000026A0\U0000FE0F  Opción inválida.")

# ---------- Buscar ----------
def buscar_grupos(_unused):
    print("\n\U0001F50D  Buscar\n" + SEP)
    print("1) Buscar grupo (nombre exacto)")
    print("2) Buscar alumno (nombre parcial)")
    opcion = input("\U0001F449  Elige una opción (1 o 2): ").strip()

    if opcion == "1":
        nombre_grupo = input("\U0001F4C1  Nombre del grupo: ").strip()
        g = mgrupo.obtener_por_nombre(nombre_grupo)
        if g:
            print(f"\U00002705  Grupo: «{g['nombre']}»")
            alumnos = malumno.listar_por_grupo(g["id"])
            if alumnos:
                print("\U0001F465  Alumnos:")
                for a in alumnos:
                    print(f"   • {a['nombre']}")
            else:
                print("\U0001F6C7  (Sin alumnos)")
        else:
            print("\U0000274C  Grupo no encontrado.")

    elif opcion == "2":
        parcial = input("\U0001F464  Nombre (parcial): ").strip()
        resultados = malumno.buscar_like_por_nombre(parcial)
        if resultados:
            for a in resultados:
                print(f" • {a['nombre']}  | Grupo: {a['grupo_nombre']}")
        else:
            print("\U0000274C  No se encontraron coincidencias.")
    else:
        print("\U000026A0\U0000FE0F  Opción inválida.")

# ---------- Modificar ----------
def modificar(_unused):
    print("\n\U0001F6E0\U0000FE0F  Modificar\n" + SEP)
    print("1) Renombrar grupo")
    print("2) Renombrar alumno")
    print("3) Mover alumno a otro grupo")
    op = input("\U0001F449  Elige una opción (1-3): ").strip()

    if op == "1":
        nombre = input("\U0001F4C1  Nombre ACTUAL del grupo: ").strip()
        g = mgrupo.obtener_por_nombre(nombre)
        if not g:
            print("\U0000274C  Grupo no encontrado.")
            return
        nuevo = input("\U0000270F\U0000FE0F  Nuevo nombre para el grupo: ").strip()
        if not nuevo:
            print("\U000026A0\U0000FE0F  El nuevo nombre no puede estar vacío.")
            return
        print("\U00002705  Grupo renombrado correctamente." if mgrupo.renombrar(g["id"], nuevo)
              else "\U0000274C  No se pudo renombrar (posible duplicado).")

    elif op == "2":
        nombre_grupo = input("\U0001F4C1  Grupo donde está el alumno: ").strip()
        g = mgrupo.obtener_por_nombre(nombre_grupo)
        if not g:
            print("\U0000274C  Grupo no encontrado.")
            return
        nombre_alumno = input("\U0001F464  Nombre ACTUAL del alumno: ").strip()
        candidatos = [a for a in malumno.buscar_por_nombre(nombre_alumno) if a["grupo_id"] == g["id"]]
        if not candidatos:
            print("\U0000274C  Alumno no encontrado en ese grupo.")
            return
        a = candidatos[0]
        nuevo_nombre = input("\U0000270F\U0000FE0F  Nuevo nombre para el alumno: ").strip()
        if not nuevo_nombre:
            print("\U000026A0\U0000FE0F  El nuevo nombre no puede estar vacío.")
            return
        print("\U00002705  Alumno renombrado correctamente." if malumno.renombrar(a["id"], nuevo_nombre)
              else "\U0000274C  No se pudo renombrar al alumno.")

    elif op == "3":
        nombre_grupo = input("\U0001F4C1  Grupo ACTUAL del alumno: ").strip()
        g_origen = mgrupo.obtener_por_nombre(nombre_grupo)
        if not g_origen:
            print("\U0000274C  Grupo origen no encontrado.")
            return
        nombre_alumno = input("\U0001F464  Alumno a mover: ").strip()
        candidatos = [a for a in malumno.buscar_por_nombre(nombre_alumno) if a["grupo_id"] == g_origen["id"]]
        if not candidatos:
            print("\U0000274C  Alumno no encontrado en ese grupo.")
            return
        a = candidatos[0]
        destino_nombre = input("\U0001F4C1  Grupo DESTINO: ").strip()
        g_destino = mgrupo.obtener_por_nombre(destino_nombre)
        if not g_destino:
            if obtener_SI_NO("\U0001F195  El grupo destino no existe. ¿Crearlo? (SI/NO): ") == "SI":
                g_destino_id = mgrupo.crear(destino_nombre)
            else:
                print("\u21A9\U0000FE0F  Operación cancelada.")
                return
        else:
            g_destino_id = g_destino["id"]
        print(f"\U00002705  Alumno movido a «{destino_nombre}»."
              if malumno.mover_de_grupo(a["id"], g_destino_id)
              else "\U0000274C  No se pudo mover al alumno.")
    else:
        print("\U000026A0\U0000FE0F  Opción inválida.")

# ---------- Vaciar ----------
def vaciar_grupos(_unused):
    print("\n\U0001F9F9  Vaciar todo\n" + SEP)
    print("\U000026A0\U0000FE0F  Esta acción borrará TODOS los grupos y alumnos.")
    if input("¿Deseas continuar? (SI/NO): ").strip().upper() == "SI":
        from conexionBD import conexion, cursor
        cursor.execute("DELETE FROM grupos")  # ON DELETE CASCADE borra alumnos
        conexion.commit()
        print("\U0001F5D1\U0000FE0F  Datos eliminados.")


def exportar_datos():
    """Exporta todos los grupos y alumnos a Excel y/o PDF."""
    grupos = mgrupo.listar()
    if not grupos:
        print("\U0000274C  No hay datos para exportar.")
        return

    print("\n\U0001F4C4  Exportar datos\n" + SEP)
    formatos = input("¿A qué formato deseas exportar? (EXCEL/PDF/AMBOS): ").strip().upper()

    # ---------- Excel ----------
    if formatos in ("EXCEL", "AMBOS"):
        wb = Workbook()
        ws = wb.active
        ws.title = "Grupos y Alumnos"
        ws.append(["Grupo", "Alumno"])
        for g in grupos:
            alumnos = malumno.listar_por_grupo(g["id"])
            if alumnos:
                for a in alumnos:
                    ws.append([g["nombre"], a["nombre"]])
            else:
                ws.append([g["nombre"], "(Sin alumnos)"])
        wb.save("reporte_grupos.xlsx")
        print("\U0001F4BE  Datos exportados a 'reporte_grupos.xlsx'.")

    # ---------- PDF ----------
    if formatos in ("PDF", "AMBOS"):
        doc = SimpleDocTemplate("reporte_grupos.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        story.append(Paragraph("Reporte de Grupos y Alumnos", styles['Title']))
        story.append(Spacer(1, 12))
        for g in grupos:
            story.append(Paragraph(f"Grupo: {g['nombre']}", styles['Heading2']))
            alumnos = malumno.listar_por_grupo(g["id"])
            if alumnos:
                for a in alumnos:
                    story.append(Paragraph(f" - {a['nombre']}", styles['Normal']))
            else:
                story.append(Paragraph("(Sin alumnos)", styles['Normal']))
            story.append(Spacer(1, 8))
        doc.build(story)
        print("\U0001F4BE  Datos exportados a 'reporte_grupos.pdf'.")