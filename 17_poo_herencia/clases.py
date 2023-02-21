class Personas:

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    
    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "estoy caminando"
    
    def dormir(self):
        return "estoy durmiendo"
    
class Informatico(Personas):
    """
    lenguajes
    experiencias
    """
    
    def __init__(self):
        self.lenguajes = "html, css, javascript, php"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "estoy programando"
    
    def repararPC(self):
        return "reparando PC"
