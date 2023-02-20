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
