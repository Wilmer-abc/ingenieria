from flask import Flask, render_template, request, redirect, url_for, flash 
from alumnos import agregar_alumno, actualizar_alumno, eliminar_alumno, obtener_alumno
from estadisticas import obtener_estadisticas_edad
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) 

@app.route("/")
def index():
    estadisticas = obtener_estadisticas_edad()  
    return render_template("index.html", estadisticas=estadisticas)

@app.route("/agregar", methods=["POST"])
def agregar():
    carnet1 = request.form["carnet1"]
    carnet2 = request.form["carnet2"]
    carnet3 = request.form["carnet3"]
    primer_nombre = request.form["PrimerNombre"]
    segundo_nombre = request.form["SegundoNombre"]
    primer_apellido = request.form["PrimerApellido"]
    segundo_apellido = request.form["SegundoApellido"]
    telefono = request.form["Telefono"]
    correo = request.form["CorreoElectronico"]
    pagado = request.form["Pagado"]
    fecha_nacimiento = request.form["FechaNacimiento"] 
    
    agregar_alumno(carnet1, carnet2, carnet3, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nacimiento)

    flash("Estudiante agregado exitosamente.")  
    return redirect(url_for("index"))

@app.route("/buscar", methods=["POST"])
def buscar():
    carnet1 = request.form.get("carnet1")
    carnet2 = request.form.get("carnet2")
    carnet3 = request.form.get("carnet3")

    if not carnet1 or not carnet2 or not carnet3:
        flash("Debes ingresar todos los valores del carnet.")
        return redirect(url_for("index"))

    alumno = obtener_alumno(carnet1, carnet2, carnet3)  

    if alumno:
        return render_template("editar.html", alumno=alumno)
    else:
        flash("Alumno no encontrado.")
        return redirect(url_for("index"))  

@app.route("/actualizar", methods=["POST"])
def actualizar():
    carnet1 = request.form["carnet1"]
    carnet2 = request.form["carnet2"]
    carnet3 = request.form["carnet3"]
    primer_nombre = request.form["PrimerNombre"]
    segundo_nombre = request.form["SegundoNombre"]
    primer_apellido = request.form["PrimerApellido"]
    segundo_apellido = request.form["SegundoApellido"]
    telefono = request.form["Telefono"]
    correo = request.form["CorreoElectronico"]
    pagado = request.form["Pagado"]
    fecha_nacimiento = request.form["FechaNacimiento"]  

    actualizar_alumno(carnet1, carnet2, carnet3, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nacimiento)

    flash("Estudiante actualizado correctamente.")  
    return redirect(url_for("index"))

@app.route("/eliminar", methods=["POST"])
def eliminar():
    carnet1 = request.form["carnet1"]
    carnet2 = request.form["carnet2"]
    carnet3 = request.form["carnet3"]

    alumno = obtener_alumno(carnet1, carnet2, carnet3)

    if alumno:
        eliminar_alumno(carnet1, carnet2, carnet3)
        flash("Estudiante eliminado con éxito.")
    else:
        flash("Este alumno no existe.")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
