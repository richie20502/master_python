import mimodulo

print(mimodulo.holaMundo("nombre"))

cad=mimodulo.calculadora(5,6,True)
print(cad)


from mimodulo import holaMundo

print(holaMundo("nononon"))

#modulo fecha
import datetime
print(datetime.date.today())
fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

#modulo de matematicas

import math

print("raiz :", math.sqrt(10))
print("pi:", float(math.pi))
print("redondear:", math.floor(8.999))

#modulo random

import random

print("aleatorio del 10 al 20: ", random.randint(10,20))