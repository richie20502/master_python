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

conexion.commit()

#cerrar conexion
conexion.close()
