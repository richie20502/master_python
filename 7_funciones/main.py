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
