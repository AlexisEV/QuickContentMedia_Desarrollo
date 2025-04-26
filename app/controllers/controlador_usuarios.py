from domain.entities.usuario import Usuario

class ControladorUsuarios:

    def registrar_usuario(self, nombre, correo):
        usuario = Usuario.registrar(nombre, correo)
        return f"Usuario {usuario.nombre} registrado exitosamente."

    def buscar_usuario(self, nombre):
        usuario = Usuario.buscar_por_nombre(nombre)
        if usuario:
            return f"Bienvenido {usuario.nombre}"
        else:
            return "Usuario no encontrado."
