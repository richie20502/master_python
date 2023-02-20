from coche import Coche

carro = Coche("verde","nissan","tsuru",200,20,5)
carro1 = Coche("amarillo","suzuki","van",200,20,5)
carro2 = Coche("rojo","nissan","tsuru",200,20,5)


print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())


#detectar tipado

if type(carro2) == Coche:
    print("es un objeto correcto")
else:
    print("no es un objeto")