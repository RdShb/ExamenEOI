from flask import Flask, request, render_template
from clases.clases import Estaciones, Primavera, Verano, Otoño, Invierno

app = Flask(__name__,template_folder='html')

@app.route("/")
def estacions():
    return render_template("start_estaciones.html")

@app.route("/estaciones", methods=['POST'])
def mostrar_estaciones():
    ### Tal vez el error esta al tomar datos?
    nombre = request.form["estacion"]
    temperatura_media = request.form["temperatura_media"]
    if nombre == "primavera":
        flores = request.form["flores"]
        primavera = Primavera(nombre,temperatura_media,flores)
        estac = primavera
    elif nombre == "otoño":
        colores = request.form["colores"]
        otoño = Otoño(nombre,temperatura_media,colores)
        estac = otoño
    elif nombre == "verano":
        actividades = request.form["actividades"]
        verano = Verano(nombre,temperatura_media,actividades)
        estac = verano
    elif nombre == "invierno":
        nieve = request.form["nieve"]
        invierno = Invierno(nombre,temperatura_media,nieve)
        estac = invierno
    ## O a pasarlos a estaciones.html
    return render_template("estaciones.html", estacion = estac)

if __name__ == '__main__':
   app.run()