# ejemplo 1
def muestraNombre():
    print("nombre 1")
    print("nombre 2")
    print("nombre 3")
    print("nombre 4")
    print("nombre 5")
    print("nombre 6")


#invocar funcion
muestraNombre()

#ejemplo 2
def mostrarTuNombre(nombre, edad):
    print(f"tu nombre es: {nombre}")

    if edad >= 18:
        print("ya eres mayor de edad")
    else:
        print("eres menor de edad")

nombre = input("cual es tu nombre ?")
edad = int(input("Cuantos años tienes ?"))

mostrarTuNombre(nombre,edad)

#ejercicio 3

def tabla(numero):
    for con in range(11):
        ope = numero*con
        print(f"{numero} x {con}  =  {ope}")
    
    print("\n")

#ejercicio 3.1
tabla(4)
for numero_t in range(1, 11):
    tabla(numero_t)

#ejercicio numero 4
#parametros opcionales
def getEmpledo(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")


getEmpledo("jose", 9876)