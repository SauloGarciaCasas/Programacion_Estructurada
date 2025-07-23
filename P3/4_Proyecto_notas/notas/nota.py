from conexionBD import *

def crear(usuario_id, titulo, descripcion):
    try:
        sql="insert into notas (usuario_id, titulo, descripcion, fecha) values (%s, %s, %s, NOW())"
        val=(usuario_id, titulo, descripcion)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        sql = "select * from notas where usuario_id=%s"
        val = (usuario_id,)
        cursor.execute(sql, val)
        return cursor.fetchall()
    except:
        return []
    
def cambiar(id, titulo, descripcion):
    try:
        cursor.execute("update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s", (titulo, descripcion, id))

        return True
    except:
        return False
    
def borrar(id):
    try:
        cursor.execute("delete from notas where id=%s", (id,))
        conexion.commit()
        return True
    except:
        return False
