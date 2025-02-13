import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ingenieria"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
        else:
            print("No se pudo conectar a la base de datos")
            return None
    except mysql.connector.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        return None
