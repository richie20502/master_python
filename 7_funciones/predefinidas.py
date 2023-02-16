nombre = "Aqui va tu nombre"

#funciones generales
print(type(nombre))

#Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Es un string")
else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("la variable es una variable int")


#limpiar espacion
frase = "aqui       espacios"
print(frase)
print("\n")
print(frase.strip())

# eliminar variables
year = 2022
print(year)
del year
print(year)
#comprobar variables vacias

texto = " tt "
if len(texto) <= 0:
    print("la variable esta vacia")
else:
    print("la variable tiene algo ")

#Encontrar caracteres
frase = "como esta boot"
print( frase.find("esta"))

#Remplazar palabras en un string
nueva_frase = frase.replace("esta", "estamos")
print(nueva_frase)

#MAyusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())