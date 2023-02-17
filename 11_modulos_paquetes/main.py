import mimodulo

print(mimodulo.holaMundo("nombre"))

cad=mimodulo.calculadora(5,6,True)
print(cad)


from mimodulo import holaMundo

print(holaMundo("nononon"))

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