from entidad.db import get_connection

class Administrador:
    def __init__(self):
        pass

    @staticmethod
    def buscarAdministrador(id_usuario):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT acceso FROM ADMINISTRADOR WHERE id_usuario=%s
            """, (id_usuario,))
            row = cur.fetchone()
            if row:
                return {
                    "acceso": row[0]
                }
            return None

    @staticmethod
    def getDatosAdministradorPorId(id_usuario):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    u.id_usuario,
                    u.username,
                    u.nombre,
                    u.apellido,
                    u.contrasena,
                    a.acceso
                FROM USUARIO u
                JOIN ADMINISTRADOR a ON u.id_usuario = a.id_usuario
                WHERE u.id_usuario = %s;
            """, (id_usuario,))
            row = cur.fetchone()
            if row:
                return {
                    "id_usuario": row[0],
                    "username": row[1],
                    "nombre": row[2],
                    "apellido": row[3],
                    "contrasena": row[4],
                    "acceso": row[5]
                }
            return None
