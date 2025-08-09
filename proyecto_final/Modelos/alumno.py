from conexionBD import conexion, cursor

def crear(nombre: str, id_grupo: int) -> int:
    cursor.execute(
        "INSERT INTO alumnos (nombre, grupo_id) VALUES (%s, %s)",
        (nombre, id_grupo)
    )
    conexion.commit()
    return cursor.lastrowid

def listar_por_grupo(id_grupo: int):
    cursor.execute(
        "SELECT id, nombre, fecha FROM alumnos WHERE grupo_id=%s ORDER BY id",
        (id_grupo,)
    )
    return cursor.fetchall()

def eliminar(id_alumno: int, grupo_id: int | None = None) -> bool:
    if grupo_id is None:
        cursor.execute("DELETE FROM alumnos WHERE id=%s", (id_alumno,))
    else:
        cursor.execute("DELETE FROM alumnos WHERE id=%s AND grupo_id=%s", (id_alumno, grupo_id))
    conexion.commit()
    return cursor.rowcount > 0

def buscar_por_nombre(nombre: str):
    cursor.execute(
        """SELECT a.id, a.nombre, a.fecha, g.id AS grupo_id, g.nombre AS grupo_nombre
           FROM alumnos a
           JOIN grupos g ON g.id = a.grupo_id
           WHERE LOWER(a.nombre)=LOWER(%s)""",
        (nombre,)
    )
    return cursor.fetchall()

def buscar_like_por_nombre(parcial: str):
    """Búsqueda parcial insensible a mayúsculas."""
    patron = f"%{parcial}%"
    # Opción A: usando COLLATE (si tu BD está en utf8mb4_unicode_ci)
    try:
        cursor.execute(
            """SELECT a.id, a.nombre, a.fecha, g.id AS grupo_id, g.nombre AS grupo_nombre
               FROM alumnos a
               JOIN grupos g ON g.id = a.grupo_id
               WHERE a.nombre LIKE %s COLLATE utf8mb4_unicode_ci
               ORDER BY a.nombre, a.id""",
            (patron,)
        )
    except Exception:
        # Opción B (fallback): usando LOWER() por si hay conflicto de colaciones
        cursor.execute(
            """SELECT a.id, a.nombre, a.fecha, g.id AS grupo_id, g.nombre AS grupo_nombre
               FROM alumnos a
               JOIN grupos g ON g.id = a.grupo_id
               WHERE LOWER(a.nombre) LIKE LOWER(%s)
               ORDER BY a.nombre, a.id""",
            (patron,)
        )
    return cursor.fetchall()