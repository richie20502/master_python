from io import open
import pathlib
# modulo para copiaer archivos
import shutil

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


#copiar archivo 


direc_original = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
direc_nueva = str(pathlib.Path().absolute()) + '/fichero_copia.txt'

shutil.copyfile(direc_original, direc_nueva)

#Eliminar
#import os

#direc_nueva = str(pathlib.Path().absolute()) + '/fichero_copia.txt'
#os.remove(direc_nueva)