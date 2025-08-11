from conexionBD import conexion, cursor

def crear(nombre: str, usuario_id: int) -> int:
    cursor.execute("INSERT INTO grupos (nombre, usuario_id) VALUES (%s, %s)", (nombre, usuario_id))
    conexion.commit()
    return cursor.lastrowid

def listar(usuario_id: int):
    cursor.execute("SELECT id, nombre, fecha FROM grupos WHERE usuario_id=%s ORDER BY id", (usuario_id,))
    return cursor.fetchall()

def obtener_por_nombre(nombre: str, usuario_id: int):
    cursor.execute(
        "SELECT id, nombre, fecha FROM grupos WHERE LOWER(nombre)=LOWER(%s) AND usuario_id=%s",
        (nombre, usuario_id)
    )
    return cursor.fetchone()

def existe_nombre(nombre: str, usuario_id: int) -> bool:
    cursor.execute(
        "SELECT id FROM grupos WHERE LOWER(nombre)=LOWER(%s) AND usuario_id=%s",
        (nombre, usuario_id)
    )
    return cursor.fetchone() is not None

def renombrar(id_grupo: int, nuevo_nombre: str, usuario_id: int) -> bool:
    if existe_nombre(nuevo_nombre, usuario_id):
        return False
    cursor.execute(
        "UPDATE grupos SET nombre=%s WHERE id=%s AND usuario_id=%s",
        (nuevo_nombre, id_grupo, usuario_id)
    )
    conexion.commit()
    return cursor.rowcount > 0

def eliminar(id_grupo: int, usuario_id: int) -> bool:
    cursor.execute("DELETE FROM grupos WHERE id=%s AND usuario_id=%s", (id_grupo, usuario_id))
    conexion.commit()
    return cursor.rowcount > 0
