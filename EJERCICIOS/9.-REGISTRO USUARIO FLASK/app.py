#importar el modulo Flask de la libreria
from flask import Flask,render_template

#crear instancia
app = Flask(__name__)

#Definir ruta
@app.route('/')
def index():
    variable = "Python"
    variable2 = 3
    return """<h1>Hola {0} {1}</h1>.format(variable,variable2)


#print(__name__)
#Ejercutar archivo principal
if __name__ == '__main__':
    app.run(debug=True,port=8000)