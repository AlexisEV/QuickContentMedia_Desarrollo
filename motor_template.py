
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

template_dir = os.path.join(os.path.dirname(__file__), "vistas")
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(["html", "xml"])
)

def render_template(nombre_template, contexto=None):
    contexto = contexto or {}
    template = env.get_template(nombre_template)
    return template.render(**contexto)

