
#Crear clase
class Persona:

    #atributos
    nombre = ""
    edad = 0
    peso = 0.0
    pais_ciudad_region = ""
    sexo = ''
    casado = False

    #constructor
    def __init__(self,nombre,edad,peso,pais,sexo,casado):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.pais = pais
        self.sexo = sexo
        self.casado = casado


    #Getters and Setters

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad

    def getPeso(self):
        return self.peso

    def getPais(self):
        return self.pais
    
    def getSexo(self):
        return self.sexo
    
    def getCasado(self):
        return self.casado
    
    def setNombre(self,nombre):
        self.nombre = nombre
    

    #Mostrar Información
    def informacionPersona(self):
        print("______Información de Usuario_______")
        print("")
        print("Nombre: {}".format(self.getNombre()))
        print("Edad: {}".format(self.getEdad()))
        print("Peso: {}".format(self.getPeso()))
        print("Pais: {}".format(self.getPais()))
        print("Sexo: {}".format(self.getSexo()))
        print("Casado: {}".format(self.getCasado()))

