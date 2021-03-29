#https://www.delftstack.com/es/howto/python/how-to-get-the-current-time-in-python/#:~:text=strftime%20para%20obtener%20la%20hora%20actual%20en%20Python&text=Como%20su%20nombre%20indica%2C%20time,la%20hora%20UTC%2C%20entonces%20time.
import time
fechaHora =time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())

print(fechaHora)

fecha = time.strftime('%d-%m-%Y')
hora = time.strftime('%H:%M:%S',time.localtime())

print(fecha)
print(hora)
