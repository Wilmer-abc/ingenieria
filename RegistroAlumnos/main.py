from interfaz import interfaz
from main import app  
import secrets

app.secret_key = secrets.token_hex(16)

if __name__ == "__main__":
    interfaz()
