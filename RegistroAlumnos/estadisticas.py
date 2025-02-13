from db import conectar_bd

def obtener_estadisticas_edad():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        sql = "SELECT YEAR(CURDATE()) - YEAR(FechaNacimiento) AS edad, COUNT(*) FROM alumnos GROUP BY edad"
        cursor.execute(sql)
        estadisticas = cursor.fetchall()
        conexion.close()
        return estadisticas
