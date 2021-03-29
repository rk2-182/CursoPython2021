from tkinter import *

class Programa:

    #Constructor
    def __init__(self):
        self.titulo = "GUI con Python"
        self.icono = '13.-GUI\img\python2.ico'
        self.icono_alt = "C:/Python/CursoPython/13.-GUI/img/python2.ico"
        self.tamaño = "720x480"
        self.ajustable = False

    def Cargar(self):
        #instanciar objeto Tk
        ventana = Tk()

        self.ventana = ventana

        ventana.title(self.titulo)
        ventana.iconbitmap(self.icono)
        ventana.geometry(self.tamaño)

        if self.ajustable == True:

            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        #metodo para mantener ventana ejecutandose
        #ventana.mainloop()
    
    def addTexto(self):
        texto = Label(self.ventana, text="Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código")
        texto.pack()

    
    def mostrar(self):
        #metodo para mantener ventana ejecutandose
        self.ventana.mainloop()
    

#Bloque principal
programa = Programa()


programa.Cargar()
programa.addTexto()
programa.mostrar()