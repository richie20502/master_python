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

#cursor.execute("""INSERT INTO vehiculos VALUES(null, 'opel','astra',23345)""")

coches = [
    ('seat', 'ibiza', 7888 ),
    ('renault', 'clio', 6788 ),
    ('citro', 'sxsx', 78976 ),
    ('mercedes', 'clase r', 56787 ),
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("---- TODOS LOS CARROS ----")
for coche in result:
    print(coche)