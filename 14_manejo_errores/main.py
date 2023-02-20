try:
    nombre = input("Cual es tu nombre?:")

    if len(nombre) > 1:
        nombre_u = "El nombre es " + nombre
    print(nombre_u)

except:
    print("ha ocurrido un error, ingresa bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("fin de la iteracion")


#Manejo de multiples excepciones
try:
    numero = int(input("Numero para elevar al cuadro: "))
    print("El cuadrado es: " + str(numero*numero))
except TypeError:
    print("Debes de convertir tus cadenas a enteros en el codigo !!")
except ValueError:
    print("introduce un numero correcto !!")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ",type(e).__name__)

#excepciones personalizadas
try:
    nombre = input("ingresa el nombre")
    edad= input("ingresa edad")

    if edad < 5  or edad > 110:
        raise ValueError("La edad introduccida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print("Bienvenido !!")
except ValueError:
    print("introduce los datos correctos")
except Exception as e:
    print("Existe error", e)
