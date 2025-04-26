class InterfazLogin:

    def mostrar_formulario(self):
        with open('static/html/login.html', 'r', encoding='utf-8') as f:
            return f.read()

    def mostrar_bienvenida(self, mensaje):
        return f"<html><body><h1>{mensaje}</h1></body></html>"
