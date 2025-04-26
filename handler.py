from infrastructure.utils.router import route_get, route_post
from app.controllers.controlador_usuarios import ControladorUsuarios
from app.interfaces.interfaz_login import InterfazLogin

controlador = ControladorUsuarios()
interfaz = InterfazLogin()

from http.server import BaseHTTPRequestHandler
from infrastructure.utils.router import routes_get, routes_post
from infrastructure.utils.helpers import responder_html, responder_json

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith('/css/'):
            self.servir_archivo_estatico('static' + self.path)
        elif self.path.startswith('/html/'):
            self.servir_archivo_estatico('static' + self.path)
        elif self.path.startswith('/js/'):
            self.servir_archivo_estatico('static' + self.path)
        else:
            handler_func = routes_get.get(self.path)
            if handler_func:
                handler_func(self)
            else:
                self.not_found()

    def do_POST(self):
        handler_func = routes_post.get(self.path)
        if handler_func:
            handler_func(self)
        else:
            self.not_found()

    def leer_json(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        import json
        return json.loads(post_data)

    def servir_archivo_estatico(self, ruta_archivo):
        try:
            if ruta_archivo.endswith('.css'):
                content_type = 'text/css'
            elif ruta_archivo.endswith('.js'):
                content_type = 'application/javascript'
            elif ruta_archivo.endswith('.html'):
                content_type = 'text/html'
            else:
                content_type = 'application/octet-stream'

            with open(ruta_archivo, 'rb') as f:
                contenido = f.read()

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.end_headers()
            self.wfile.write(contenido)

        except FileNotFoundError:
            self.not_found()

    def not_found(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'Not Found')


@route_get('/')
def mostrar_formulario(handler):
    contenido = interfaz.mostrar_formulario()
    responder_html(handler, contenido)

@route_post('/api/login')
def login(handler):
    datos = handler.leer_json()
    respuesta = controlador.buscar_usuario(datos['nombre'])
    html = interfaz.mostrar_bienvenida(respuesta)
    responder_html(handler, html)

@route_post('/api/registro')
def registro(handler):
    datos = handler.leer_json()
    respuesta = controlador.registrar_usuario(datos['nombre'], datos['correo'])
    html = interfaz.mostrar_bienvenida(respuesta)
    responder_html(handler, html)
