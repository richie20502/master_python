#importamos 
import sqlite3

#conexion
conexion = sqlite3.connect('prueba.db')

#conexion cursos
cursor = conexion.cursor()

#craete tabla

cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTORS("+
"id int(10) auto_increment not null,"+
"titulo varchar(255), "+
"descripcion text"+
"precio int(255)"+
")")

#guardar cambios
conexion.commit()

#insertar datos
cursor.execute("INSERT INTO productos VALUES(null, 'primer producto', 'Descripcion de', 200)")

#guardar cambios
conexion.commit()
cursor.execute("SELECT * FROM productos;")
productos= cursor.fetchall()

for producto in productos:
    print(producto)

#cerrar conexion
conexion.close()
