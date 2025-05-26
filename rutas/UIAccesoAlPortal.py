
from router import route, redirect
from motor_template import render_template
from control.gestorUsuario import GestorUsuario

@route("/", method="GET")
@route("/mostrarLogin", method="GET")
def mostrarlogin(params):
    return render_template("UIAccesoPortal.html")

@route("/procesarLogin", method="POST")
def procesarlogin(params):
    usuario = params.get("usuario", [""])[0].strip()
    contrasena = params.get("contrasena", [""])[0].strip()
    resultado = GestorUsuario().validarCredenciales(usuario, contrasena)

    if resultado["estado"] == "cliente":
        return redirect("/mostrarCliente", cookies={"id_usuario": str(resultado["datos"]["id_usuario"])})

    if resultado["estado"] == "administrador":
        return redirect("/admin/mostrarUIInicioAdmin", cookies={"id_usuario": str(resultado["datos"]["id_usuario"])})

    return render_template("UIAccesoPortal.html", {"mensaje": resultado["mensaje"]})
