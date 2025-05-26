from control import gestorUsuario
from router import route, redirect
from motor_template import render_template
from control.gestorUsuario import GestorUsuario

@route("/admin/mostrarAdministrarCliente", method="GET")
def mostrarAdministrarCliente(params):
    cookies = params.get("__cookies__", {})
    errorBuscar = int(cookies.get("errorBuscar"))
    listClientes = GestorUsuario.getClientes()
    return render_template("UIAdministrarCliente.html", {"listClientes": listClientes,
        "errorBuscar": errorBuscar})


@route("/admin/buscarClientePorID", method="POST")
def adminBuscarClientePorID(params):
    id_cliente = params.get("id_cliente", [""])[0].strip()
    datosCliente = gestorUsuario.getDatosClientePorId(id_cliente)
    if datosCliente:
        return render_template("UIAdministrarCliente.html", {"listClientes": datosCliente})
    else:
        return redirect("/admin/mostrarAdministrarCliente", cookies={ "errorBuscar": "El cliente no existe" })


@route("/admin/mostrarHistorialCliente", method="POST")
def mostrarHistorialCliente(params):
    id_cliente = params.get("id_cliente", [""])[0].strip()


@route("/admin/modificarSaldoCliente", method="POST")
def modificarSaldoCliente(params):
    id_cliente = params.get("id_cliente", [""])[0].strip()
