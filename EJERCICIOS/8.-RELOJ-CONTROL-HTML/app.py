#http://elclubdelautodidacta.es/wp/2012/06/mysql-ha-llegado-la-hora/
#https://stackoverflow.com/questions/17873820/flask-url-for-with-multiple-parameters

#importar flask (clase)
from flask import Flask,render_template,url_for,request,flash,redirect
from flask_mysqldb import MySQL
import time

#el valor de la variable sera igual al nombre del modulo python
app = Flask(__name__)


#conexión BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'empresa'

mysql = MySQL(app)
#**************************************************************

app.secret_key = 'some_secret' #palabra secreta para mensjes flash

#print(app)
#print(__name__)
@app.route('/')
def index():
    
    cursor = mysql.connect.cursor()
    sql = "SELECT * FROM reloj"
    cursor.execute(sql)
    datos = cursor.fetchall()
    #print(datos)
    return render_template('reloj.html', contacts = datos)

#********Insertar****************
@app.route('/entrada', methods=['GET', 'POST'])
def entrada():
    if request.method == "POST":
        #id = request.form['id']
        nombreU = request.form['nombre']
        fecha = time.strftime('%Y-%m-%d')
        entrada  = time.strftime('%H:%M:%S',time.localtime())
        salida  = time.strftime('%H:%M:%S',time.localtime())

        salida = 'null'

        # insertar datos en DB
        sql = "insert into reloj (nombre,fecha,entrada,salida) values(%s,%s,%s,%s)"
        values = (nombreU, fecha,entrada,salida)

        cursor = mysql.connect.cursor()
        cursor.execute(sql, values)
        if cursor.rowcount == 1 and len(nombreU) !=0:
            cursor.connection.commit()
            flash("Ingreso con exito")
            return redirect(url_for('index')) #se indica el metodo
        else:
            flash("Error al registrar los datos")

#********Insertar****************
@app.route('/salida', methods=['GET', 'POST'])
def salida():
    if request.method == "POST":
        #id = request.form['id']
        nombreU = request.form['nombre']
        fecha = time.strftime('%Y-%m-%d')
        entrada  = time.strftime('%H:%M:%S',time.localtime())
        salida  = time.strftime('%H:%M:%S',time.localtime())

        entrada = 'null'

        # insertar datos en DB
        sql = "insert into reloj (nombre,fecha,entrada,salida) values(%s,%s,%s,%s)"
        values = (nombreU, fecha,entrada,salida)

        cursor = mysql.connect.cursor()
        cursor.execute(sql, values)
        if cursor.rowcount == 1 and len(nombreU) !=0:
            cursor.connection.commit()
            flash("Adios!")
            return redirect(url_for('index')) #se indica el metodo
        else:
            flash("Error al registrar los datos")

@app.route('/editar_entrada/<id>', methods=['GET', 'POST'])
def editar(id):
    cursor = mysql.connect.cursor()
    sql = "SELECT * FROM reloj WHERE id = {0}".format(id)
    cursor.execute(sql)
    datos = cursor.fetchall()
    return render_template('entrada.html',contact = datos[0])

@app.route('/editar_salida/<id>', methods=['GET', 'POST'])
def editar_salida(id):
    cursor = mysql.connect.cursor()
    sql = "SELECT * FROM reloj WHERE id = {0}".format(id)
    cursor.execute(sql)
    datos = cursor.fetchall()
    return render_template('salida.html',contact = datos[0])
    
@app.route('/eliminar/<string:id>')
def eliminar(id):
    sql = "DELETE FROM reloj WHERE id = {0}".format(id)
    cursor = mysql.connect.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        cursor.connection.commit()
        flash("Registro eliminado  exitosamente!")
        return redirect(url_for('index')) #se indica el metodo
    else:
        flash("Error al eliminar")


@app.route('/modificar_entrada/<id>', methods=['GET', 'POST'])
def modificar(id):
     if request.method == "POST":
        entrada = request.form['entrada']
        cursor = mysql.connect.cursor()
        cursor.execute("""UPDATE reloj SET entrada = %s WHERE id=%s""",(entrada,id))

        if cursor.rowcount == 1:
            cursor.connection.commit()
            flash("Dato Actualizado")
            return redirect(url_for('index'))
        else:
            flash("Error al actualizar")

@app.route('/modificar_salida/<id>', methods=['GET', 'POST'])
def modificar_salida(id):
     if request.method == "POST":
        salida = request.form['salida']
        cursor = mysql.connect.cursor()
        cursor.execute("""UPDATE reloj SET salida = %s WHERE id=%s""",(salida,id))

        if cursor.rowcount == 1:
            cursor.connection.commit()
            flash("Registro manual de salida registrado")
            return redirect(url_for('index'))
        else:
            flash("Error al actualizar")



#el modulo al momento de ejeuctarse se transforma en el modulo principal '__main__'
if __name__ == '__main__':
    app.run(debug=True)