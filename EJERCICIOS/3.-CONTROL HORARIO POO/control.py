from meses_2021 import Meses_2021
#********librerias para correo***************
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
#*********************************************

#Libreria para audio
from playsound import playsound

import os


class Control:
    # atributos
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio']
    dias = ['lunes', 'martes', 'miercoles',
        'jueves', 'viernes', 'sabado', 'domingo']
    datos_almacenados = {}

    salida_general = 17
    salida_viernes = 16

    # Constructor de la clase
    def __init__(self):
        self.mes = ''
        self.fecha = ''
        self.entrada = 0
        self.salida = 0
        self.caputra_dia = ''
        self.horas_extras_general = 0
        self.horas_extras_viernes = 0
        self.horas_extras_sabado = 0

    # Getters

    def getMes(self):
        return self.mes

    def getFecha(self):
        return self.fecha

    def getEntrada(self):
        return self.entrada

    def getSalida(self):
        return self.salida

    def ValidarMes(self):
        intentos = 0
        while intentos < 3:
            mes = input("Ingrese el mes: ")
            mes_capitalizado = mes.capitalize()

            if mes_capitalizado in self.meses:
                print("Mes encontrado")
                self.mes = mes_capitalizado
                self.ValidarFecha()
                self.Ingreso()
                self.Salida()
                break

            else:
                print("Mes no existente, vuelva a intentarlo")
                intentos += 1

        if intentos > 3:
            print("Fin de intentos")

    # **********************Metodo para validar dias del mes*********************************

    def ValidarFecha(self):
        while True:
            dia = input("Ingrese el dia (formato: dia 00)")
            self.caputra_dia = dia[0]
            
            # crear instancia de la clase meses2021 y usar sus fechas
            meses01 = Meses_2021()
            mes_buscado = meses01.meses(self.mes)

            if dia in mes_buscado:
                print("El dia existe")
                self.fecha = dia #asignar dia y fecha
                break
            else:
                print("El dia ingresado no existe")
                self.fecha = 'fecha invalida'

    def Ingreso(self):
        while True:
            entrada = float(input("Ingrese horario entrada (ej: 8.00): "))
            if entrada > 04.00:
                self.entrada = entrada
                #self.datos_almacenados[entrada]
                break
            else:
                print("Horario no autorizado!")

    def Salida(self):
        while True:
            salida = float(input("Ingrese horario salida: "))
            if salida <24.59:
                self.salida = salida
                self.datos_almacenados[self.fecha] = salida
                break
            else:
                print("Horario no valido!")

    def horas_extras(self):
        print("")
        if self.caputra_dia == 'l' or self.caputra_dia == 'm' or self.caputra_dia == 'm' or self.caputra_dia == 'j':
            # Calcualr horas extras trabajadas si dia equivale de lunes a jueves es 17:00 salida - salida_funcionario
            horas_extras_g= self.salida - self.salida_general
            # Redondear a 2 digitos
            self.horas_extras_general = round(horas_extras_g,3)

            print("Horas extras trabajadas el dia {} fueron: {} a partir de las 17:00 hrs.".format(self.fecha,self.horas_extras_general))
        
        elif self.caputra_dia == 'v':
            horas_extras_Viernes = self.salida - self.salida_viernes
            self.horas_extras_viernes = round(horas_extras_Viernes,3)
            print("Horas extras trabajdas el dia {} fueron: {} a partir de las 16:00 hrs.".format(self.fecha,self.horas_extras_viernes))
        
        else:
            horas_extras_sabado = self.salida - self.entrada
            self.horas_extras_sabado = horas_extras_sabado
            print("Horas extras trabajadas el dia sabado fueron: {}".format(self.horas_extras_sabado))
        
    

    # Mostrar información
    def MostrarInfo(self):
        print("\n---------------------")
        print("\tTicket")
        print("---------------------")
        print(" Mes:.......{}".format(self.getMes()))
        print(" Fecha:.....{}".format(self.getFecha()))
        print(" Entrada:...{}".format(self.getEntrada()))
        print(" Salida:....{}".format(self.getSalida()))
        print("---------------------")

        archivo = open('ticket.txt','w')
        archivo.write("\tTicket\n")
        archivo.write("Mes:......{}\n".format(self.mes))
        archivo.write("Fecha:....{}\n".format(self.fecha))
        archivo.write("Entrada:..{}\n".format(self.entrada))
        archivo.write("Salida:...{}\n".format(self.salida))
        archivo.write("---------------------\n")
        archivo.close()
    
    def DatosAlmacenados(self):
        mes_actual = self.mes
        info = self.datos_almacenados
        print("\t{}".format(mes_actual))
        print(info)
    
    def EnviarCorreo(self):
        mensaje = MIMEMultipart("plain")
        mensaje["From"] = "ricardoplus@live.cl"
        mensaje["To"] = "ricardoplus@live.cl"
        mensaje["Subject"] = "Ticket Mateo SA"

        adjunto = MIMEBase("application","octect-stream")
        adjunto.set_payload(open("ticket.txt","rb").read()) #Archivo adjunto
        adjunto.add_header("content-Disposition", "attachment; filename=mensaje.txt")
        mensaje.attach(adjunto)

        #correo tipo outlook
        smtp = SMTP("smtp.live.com")
        smtp.starttls()

        #Logear
        smtp.login("ricardoplus@live.cl","negrokuzey182")
        smtp.sendmail("ricardoplus@live.cl","ricardoplus@live.cl",mensaje.as_bytes())
        smtp.quit()
        #ruta absoluta
        playsound('E:\\Curso_Python2021\\CursoPython\EJERCICIOS\\3.-CONTROL HORARIO POO\\ringtones-xperia-notification.mp3')
        #ruta relativa
        #playsound('3.-CONTROL HORARIO POO\\ringtones-xperia-notification.mp3')
        
    

 
