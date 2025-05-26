from entidad.db import get_connection

class Cliente:
    def __init__(self):
        pass

    @staticmethod
    def buscarCliente(id_usuario):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT excliente FROM CLIENTE WHERE id_usuario=%s
            """, (id_usuario,))
            row = cur.fetchone()
            if row:
                return {
                    "excliente": row[0]
                }
            return None

    @staticmethod
    def getDatosClientePorID(id_usuario):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT 
                            u.id_usuario,
                            u.username,
                            u.nombre,
                            u.apellido,
                            u.contrasena,
                            c.saldo,
                            c.excliente
                        FROM USUARIO u
                        JOIN CLIENTE c ON u.id_usuario = c.id_usuario
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
                    "saldo": row[5],
                    "excliente": row[6]
                }
            return None

    @staticmethod
    def getClientes():
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    u.id_usuario,
                    u.username,
                    u.nombre,
                    u.apellido,
                    u.contrasena,
                    c.saldo,
                    c.excliente
                FROM USUARIO u
                INNER JOIN CLIENTE c ON u.id_usuario = c.id_usuario;
            """)
            rows = cur.fetchall()
            clientes = []
            for row in rows:
                clientes.append({
                    "id_usuario": row[0],
                    "username": row[1],
                    "nombre": row[2],
                    "apellido": row[3],
                    "contrasena": row[4],
                    "saldo": row[5],
                    "excliente": row[6]
                })
            return clientes