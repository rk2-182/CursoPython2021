from meses_2021 import meses

#Horarios de salida : general = 5 de la tarde, viernes 4 de la tarde
general = 17
viernes = 16

datos_almacenados={}

print("*****Control de Horario*****")
print("")

mes_in = input("Indique el mes: ")


while True:
    mes = meses(mes_in)
    dia = input("Ingrese el dia (formato: dia 00)")
    if dia in mes:
        print("el dia existe")
        entrada = float(input("Ingrese horario entrada (ej: 8.00): "))
        salida = float(input("Ingrese horario salida: "))
        datos_almacenados[dia] = salida
        prueba = dia[0]
        #print(prueba)
        
        if prueba  == 'l' or prueba == 'm' or prueba == 'm' or prueba == 'j':
            #Calcualr horas extras trabajadas si dia equivale de lunes a jueves es 17:00 salida - salida_funcionario
            horas_extras_porDia = salida - general
             #Redondear a 2 digitos
            horas_extras = round(horas_extras_porDia,2)

            print("Horas extras trabajadas el dia {} fueron: {}".format(dia,horas_extras))
            
        elif prueba == 'v':
            horas_extras_Viernes = salida - viernes
            horas_extras_v = round(horas_extras_Viernes,2)
            print("Horas extras trabajdas el dia {} fueron: {}".format(dia,horas_extras_v))
        
        else:
            horas_extras_sabado = salida - entrada
            print("Horas extras trabajadas el dia sabado fueron: {}".format(horas_extras_sabado))
        
        
        continuar = int(input("Desea continuar? (1=Si 0=No)"))
        if continuar == 1:
            continue
            #dia = input("Ingrese el dia (formato: dia 00)")
        else:

            break
    else:
        print("No existe, reintentar")
        dia = input("Ingrese el dia (formato: dia 00)")



print("\n>>>>>Datos mes {}<<<<<".format(mes_in))
print("------------------------------------")
print(datos_almacenados)
