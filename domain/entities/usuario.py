from infrastructure.bd.conexion import obtener_conexion

class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

    @classmethod
    def registrar(cls, nombre, correo):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s) RETURNING id;"
        cursor.execute(query, (nombre, correo))
        id_usuario = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        conexion.close()
        return cls(id_usuario=id_usuario, nombre=nombre, correo=correo)

    @classmethod
    def buscar_por_nombre(cls, nombre):
        # TODO XD Ejemplo nomas
        return None
