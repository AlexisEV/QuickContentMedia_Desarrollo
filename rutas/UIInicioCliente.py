from router import route
from motor_template import render_template
from control.gestorUsuario import GestorUsuario

@route("/mostrarCliente", method="GET")
def mostrarCliente(params):
    cookies = params.get("__cookies__", {})
    id_usuario = int(cookies.get("id_usuario"))
    datosCliente = GestorUsuario.getDatosClientePorID(id_usuario)

    return render_template("UIInicioCliente.html", datosCliente["datos"])
