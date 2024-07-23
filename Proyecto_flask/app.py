from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL




app = Flask(__name__) #aplicacion

#Conexion a bd-mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'miguel'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flaskprueba'
mysql = MySQL(app)

#Conexion para guardar sesion 
app.secret_key = 'mysecretkey'

#rutas de la pagina
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from contactos')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contactos = data)

#rutas de la pagina contacto
@app.route('/add_contacto', methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        print( nombre, apellido, telefono, email)

        cursor_conexion = mysql.connection.cursor() # para meter en la tablas en mysql en la bd
        cursor_conexion.execute('INSERT INTO contactos(nombre, apellido, telefono, email) VALUES(%s, %s, %s, %s)', (nombre, apellido, telefono, email))
        mysql.connection.commit()
        flash('contacto anadido')

    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(port =3000, debug = True)