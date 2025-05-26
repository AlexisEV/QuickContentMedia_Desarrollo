from router import route
from motor_template import render_template
from control.gestorUsuario import GestorUsuario

@route("/admin/mostrarUIInicioAdmin", method="GET")
def mostrarUIInicioAdmin(params):
    cookies = params.get("__cookies__", {})
    id_usuario = int(cookies.get("id_usuario"))
    datosAdministrador = GestorUsuario.getDatosAdministradorPorId(id_usuario)

    return render_template("UIInicioAdmin.html", datosAdministrador["datos"])
