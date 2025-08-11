import bcrypt
from conexionBD import conexion, cursor

def _hash_password(password: str) -> str:
    # bcrypt genera salt internamente; resultado ~60 chars
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def registrar(nombre: str, email: str, password: str) -> int | None:
    # email único
    cursor.execute("SELECT id FROM usuarios WHERE LOWER(email)=LOWER(%s)", (email,))
    if cursor.fetchone():
        return None
    password_hash = _hash_password(password)
    cursor.execute(
        "INSERT INTO usuarios (nombre, email, password_hash) VALUES (%s, %s, %s)",
        (nombre, email, password_hash)
    )
    conexion.commit()
    return cursor.lastrowid

def login(email: str, password: str):
    # 1) busca por email
    cursor.execute(
        "SELECT id, nombre, email, password_hash FROM usuarios WHERE LOWER(email)=LOWER(%s)",
        (email,)
    )
    row = cursor.fetchone()
    if not row:
        return None
    # 2) verifica hash bcrypt
    ok = bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8"))
    if not ok:
        return None
    # 3) devuelve datos sin el hash
    return {"id": row["id"], "nombre": row["nombre"], "email": row["email"]}
