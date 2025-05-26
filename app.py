
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import rutas  # Asegura la ejecución de todos los decoradores
from router import get_handler

def parse_cookies(cookie_header):
    cookies = {}
    if not cookie_header:
        return cookies
    for pair in cookie_header.split(";"):
        if "=" in pair:
            key, value = pair.strip().split("=", 1)
            cookies[key] = value
    return cookies

class Dispatcher(BaseHTTPRequestHandler):
    def do_GET(self):
        self._handle_request("GET")

    def do_POST(self):
        self._handle_request("POST")


    def _handle_request(self, method):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parsed.query

        if method == "GET":
            params = parse_qs(query)
        elif method == "POST":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode()
            params = parse_qs(body)
        else:
            params = {}

        handler = get_handler(method, path)
        if handler:
            try:
                cookie_header = self.headers.get("Cookie", "")
                params["__cookies__"] = parse_cookies(cookie_header)
                result = handler(params)
                if isinstance(result, dict) and result.get("redirect"):
                    self.send_response(302)
                    self.send_header("Location", result["location"])
                    for key, value in result.get("cookies", {}).items():
                        self.send_header("Set-Cookie", f"{key}={value}; Path=/")
                    self.end_headers()
                else:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(result.encode("utf-8"))
            except Exception as e:
                self.send_error(500, f"Error interno del servidor: {e}")
        else:
            self.send_error(404, "Ruta no encontrada")


if __name__ == "__main__":
    try:
        servidor = HTTPServer(("0.0.0.0", 8080), Dispatcher)
        print("Servidor corriendo en http://localhost:8080")
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
