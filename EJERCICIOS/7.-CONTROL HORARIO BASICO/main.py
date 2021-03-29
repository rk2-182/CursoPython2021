
import time

class Control:
    #hora = time.strftime('%H:%M:%S',time.localtime())
    #fecha = time.strftime('%d-%m-%Y')

    def __init__(self):
        self.entrada = ''
        self.salida = ''
        self.nombre = ''
        #self.hora = time.strftime('%H:%M:%S',time.localtime())
        self.fecha = time.strftime('%d-%m-%Y')

    def Entrada(self):
        while True:
            enrty = input("PRESIONE E PARA MARCAR ENTRADA: ")
            if enrty == 'E' or enrty == 'e':
                self.entrada  = time.strftime('%H:%M:%S',time.localtime())
                print("Thank You!",self.entrada)
                break
            else:
                print("Por favor presione E para entrada")
    
    def Salida(self):
        while True:
            salir = input("PRESIONE S PARA MARCAR SALIDA: ")
            if salir == 'S' or salir=='s':
                self.salida = time.strftime('%H:%M:%S',time.localtime())
                break
            else:
                print("Por favor presione S para salida")

    def Mostrar(self):
        print("\n")
        print("\tTicket")
        print("===================")
        print(self.fecha)
        print("ENTRADA: {}".format(self.entrada))
        print("SALIDA: {}".format(self.salida))
        print("===================")

#***************Bloque principal***************
persona01 = Control()

persona01.Entrada()
persona01.Salida()
persona01.Mostrar()