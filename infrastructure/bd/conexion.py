import psycopg2

def obtener_conexion():
    return psycopg2.connect(
        host="127.0.0.1",
        port="5433",
        database="QCM",   # Asegúrate que esta base exista
        user="postgres",
        password="1234"   # Cambia si tu contraseña es diferente
    )
