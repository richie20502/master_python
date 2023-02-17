from io import open
import pathlib
#escribir archivo
direc = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
#print(direc)
archivo = open(direc, "a+")

archivo.write("**** soy un texto **** \n")
archivo.close()

# leer archivo
#abrir el archivo
direc = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
archivo_leer = open(direc, "r")

#leer el archivo
cont = archivo_leer.read()
print(cont)

#leer contenido y guardar en lista
lista = archivo_leer.readlines()
archivo_leer.close()

for frase in lista:
    print("- "+ frase)