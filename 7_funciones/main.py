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

#ejemplo 5 paramaetros opcionales y return (devolver datos)

def saludo(nombre):
    saludo = f"hola, saludos {nombre}"
    return saludo

print(saludo("Ricardo lugo"))


def calculadora(n1,n2,basicas = False):
    suma = n1 + n2
    resta = n1 - n2
    multi = n1 * n2
    divi = n1 / n2
    cadena = ""

    if basicas != False:
        cadena += "suma: " +str(suma)
        cadena += "\n"
        cadena += "resta: "+ str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion: "+str(multi)
        cadena += "\n"
        cadena += "division: "+str(divi)
        cadena += "\n"

    return cadena


cad=calculadora(5,6)
print(cad)

# ejercicio 7

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) +"  " + getApellidos(apellido)

print(devuelveTodo("Ricardo","Lugo"))

#ejemplo 8 funciones lambda

dime_el_year = lambda year: f"el año es {year*100}"

print(dime_el_year(2034))