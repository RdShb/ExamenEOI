from flask import Flask, request, render_template
from clases.clases import Estaciones, Primavera, Verano, Otoño
app = Flask(__name__,template_folder='html')

@app.route("/")
def estacions():
    return render_template("start_estaciones.html")

@app.route("/estaciones", methods=['POST'])
def mostrar_estaciones():
    nombre = request.form["estacion"]
    temperatura_media = request.form["temparatura_media"]
    actividades = request.form["actividades"]
    colores = request.form["colores"]
    flores = request.form["flores"]
    if nombre == "primavera":
        estacion = Primavera(nombre,temperatura_media,flores)
    elif nombre == "otoño":
        estacion = Otoño(nombre,temperatura_media,colores)
    elif nombre == "verano":
        estacion = Verano(nombre,temperatura_media,actividades)
    
    return render_template("estaciones.html", estacion)

if __name__ == '__main__':
   app.run()