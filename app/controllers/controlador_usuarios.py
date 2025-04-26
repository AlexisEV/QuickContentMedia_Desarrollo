from domain.entities.usuario import Usuario

class ControladorUsuarios:

    def registrar_usuario(self, nombre, correo):
        usuario = Usuario.registrar(nombre, correo)
        return f"Usuario {usuario.nombre} registrado exitosamente."
