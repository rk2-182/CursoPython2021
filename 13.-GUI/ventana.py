#Tkinter
#Modulo para crear interfaces graficas de usuario

from tkinter import *

import os.path

ventana = Tk()

#Comprobar si existe un archivo (ruta absoluta)
ruta_icono = os.path.abspath('./img/python2.ico')

#Comprobar si existe archivo
if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('C:/Python/CursoPython/13.-GUI/img/python2.ico')

#Icono de la ventana
ventana.iconbitmap("13.-GUI/img/python2.ico")

#titulo
ventana.title("Python 3 GUI")

#definir tamaño al iniciar
ventana.geometry("720x480")

#bloquear tamaño ventana
ventana.resizable(0,0)

#Mostrar texto en pantalla
texto = Label(ventana, text=ruta_icono)
texto.pack()


ventana.mainloop()