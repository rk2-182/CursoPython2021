#importar flask (clase)
from flask import Flask,render_template,url_for
from flask_mysqldb import MySQL



#el valor de la variable sera igual al nombre del modulo python
app = Flask(__name__)


#conexión BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)
#**************************************************************


#print(app)
#print(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#el modulo al momento de ejeuctarse se transforma en el modulo principal '__main__'
if __name__ == '__main__':
    app.run(debug=True)

