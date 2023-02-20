class Coche:

    #Atributos o variables
    color = "Rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    s_p = "atributo publico"
    __s_pr = "atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    #Metodos, son acciones que hace el objeto (coche)
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def getVelocidad(self):
        return self.velocidad
    
    def setCaballaje(self, caballaje):
        self.caballaje = caballaje
    
    def getCaballaje(self):
        return self.caballaje
    
    def setPlazas(self, plazas):
        self.plazas = plazas
    
    def getPlazas(self):
        return self.plazas

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):

        info = "---- Onformación del coche ----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + self.getVelocidad()

        return info
