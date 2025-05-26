from entidad.db import get_connection

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def buscarCredenciales(username, contrasena):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id_usuario FROM USUARIO WHERE username=%s AND contrasena=%s
            """, (username, contrasena))
            row = cur.fetchone()
            if row:
                return {
                    "id_usuario": row[0]
                }
            return None

    @staticmethod
    def buscarUsuarioPorUsername(username):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id_usuario FROM USUARIO WHERE username=%s
            """, (username,))
            id_usuario = cur.fetchone()
            if id_usuario:
                return {
                    "id_usuario": id_usuario[0]
                }
            return None

    @staticmethod
    def registrarCliente(nombre, apellido, username, contrasena):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO USUARIO (nombre, apellido, username, contrasena)
                VALUES (%s, %s, %s, %s)
                RETURNING id_usuario;
            """, (nombre, apellido, username, contrasena))
            id_usuario = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO CLIENTE (id_usuario, saldo, excliente)
                VALUES (%s, 0, FALSE);
            """, (id_usuario,))
            conn.commit()

            return {
                "id_usuario": id_usuario
            }
