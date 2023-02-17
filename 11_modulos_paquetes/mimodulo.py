def holaMundo(nombre):
    return f"hola , {nombre}"

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