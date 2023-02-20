class Coche:

    #Atributos o variables
    color = "Rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Metodos, son acciones que hace el objeto (coche)

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

coche = Coche()
print(coche.marca, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actual: ", coche.velocidad)

coche.frenar()
coche.frenar()
coche.frenar()

print("Velocidad actual: ", coche.velocidad)