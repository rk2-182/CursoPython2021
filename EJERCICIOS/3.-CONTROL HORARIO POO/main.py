from control import Control
import time


#Bloque principal
#Creamos la instancia de la clase control
control01 = Control()

datos = {}

while True:
    print("\nBienvenido al Sistema de Control 1.0")
    print("==========================================")
    #Ingreso y validacion del mes
    control01.ValidarMes()
    #control01.Ingreso()
    #control01.Salida()

    time.sleep(0.5)
    #Mostrar los datos de forma ordenada
    control01.MostrarInfo()
    
    respuesta = int(input("Desea ver las horas extras trabajadas? (si=1 no = 0)"))

    if respuesta == 1:
        control01.horas_extras()
    else:
        print("Que tenga un buen dia!")
    
    print("Desea repetir el proceso? (1=Si 0=No)")
    resp = int(input())

    if resp ==1:
        continue
    else:
        control01.DatosAlmacenados()
        control01.EnviarCorreo()
        break
print("----------------------------------")
salir = input(print("Presione ENTER PARA SALIR "))


