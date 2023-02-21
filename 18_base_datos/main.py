import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "master_python"
)

cursor = database.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")