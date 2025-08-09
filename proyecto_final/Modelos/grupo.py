from conexionBD import conexion, cursor

def crear(nombre: str) -> int:
    cursor.execute("INSERT INTO grupos (nombre) VALUES (%s)", (nombre,))
    conexion.commit()
    return cursor.lastrowid

def listar():
    cursor.execute("SELECT id, nombre, fecha FROM grupos ORDER BY id")
    return cursor.fetchall()

def obtener_por_nombre(nombre: str):
    cursor.execute("SELECT id, nombre, fecha FROM grupos WHERE LOWER(nombre)=LOWER(%s)", (nombre,))
    return cursor.fetchone()

def eliminar(id_grupo: int) -> bool:
    cursor.execute("DELETE FROM grupos WHERE id=%s", (id_grupo,))
    conexion.commit()
    return cursor.rowcount > 0