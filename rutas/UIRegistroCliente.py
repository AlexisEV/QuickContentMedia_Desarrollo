
from router import route, redirect
from motor_template import render_template
from control.gestorUsuario import GestorUsuario

@route("/mostrarRegistro", method="GET")
def mostrar_registro(params):
    return render_template("UIRegistroCliente.html")

@route("/procesarRegistro", method="POST")
def procesarRegistro(params):
    nombre = params.get("nombre", [""])[0].strip()
    apellido = params.get("apellido", [""])[0].strip()
    username = params.get("username", [""])[0].strip()
    contrasena = params.get("contrasena", [""])[0].strip()

    estado = GestorUsuario().registrarCliente(nombre, apellido, username, contrasena)
    if estado["estado"] == "error":
        return render_template("UIRegistroCliente.html", {"mensaje": estado["mensaje"]})

    return redirect("/mostrarCliente", cookies={"id_usuario": str(estado["datos"]["id_usuario"])})
