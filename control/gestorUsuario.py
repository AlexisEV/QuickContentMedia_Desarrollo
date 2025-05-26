from entidad.usuario import Usuario
from entidad.cliente import Cliente
from entidad.administrador import Administrador

class GestorUsuario:
    def validarCredenciales(self, usuario, contrasena):
        datosUsuario = Usuario.buscarCredenciales(usuario, contrasena)
        if not datosUsuario:
            return {
                "estado": "invalido",
                "mensaje": "Credenciales incorrectas"
            }
        datosAdministrador = Administrador.buscarAdministrador(datosUsuario["id_usuario"])
        if datosAdministrador:
            return {
                "estado": "administrador",
                "datos": datosUsuario
            }

        datosCliente = Cliente.buscarCliente(datosUsuario["id_usuario"] )
        if datosCliente["excliente"]:
            return {
                "estado": "valido",
                "mensaje": "es un excliente"
            }

        return {
            "estado": "cliente",
            "datos": datosUsuario
        }

    @staticmethod
    def getDatosAdministradorPorId(id_usuario):
        datosAdministrador = Administrador.getDatosAdministradorPorId(id_usuario)
        if datosAdministrador:
            return {
                "datos": datosAdministrador
            }

    @staticmethod
    def getDatosClientePorID(id_usuario):
        datosCliente = Cliente.getDatosClientePorID(id_usuario)
        if datosCliente:
            return {
                "datos": datosCliente
            }
        return None

    @staticmethod
    def registrarCliente(nombre, apellido, username, contrasena):
        isUsername = Usuario.buscarUsuarioPorUsername(username)
        if isUsername != None:
            return {
                "estado": "error",
                "mensaje": "El usuario ya existe"
            }

        id_usuario = Usuario.registrarCliente(nombre, apellido, username, contrasena)
        return {
            "estado": "valido",
            "datos": id_usuario
        }

    @staticmethod
    def getClientes():
        listClientes = Cliente.getClientes()
        return listClientes
        
