from interfaz import interfaz
from main import app  # Importa la app desde main.py
import secrets

app.secret_key = secrets.token_hex(16)

if __name__ == "__main__":
    interfaz()
