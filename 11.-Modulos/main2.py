""" Modulo: Un módulo le permite a usted organizar lógicamente su código Python. Agrupando código relacionado dentro de un módulo hace el código mas fácil de entender y usar. Un módulo es un objeto de Python con atributos con nombres arbitrarios que puede enlazar y hacer referencia.
    Simplemente, un módulo es no es otra cosa sino un archivo con extensión .py. Un módulo puede definir funciones, clases y variables, también puede incluir código ejecutable.
    fuente: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion8/modulos.html#:~:text=Un%20m%C3%B3dulo%20es%20un%20objeto,tambi%C3%A9n%20puede%20incluir%20c%C3%B3digo%20ejecutable."""


#importar todos las funciones del modulo utilizando *
#from calculadora import *
# utilizar solo una funcion del modulo
from calculadora import sumar


print("**********Calculadora 1.0***********\n")
print("Sumar")
print("----------")
num1 = int(input("Ingrese el primer numero a sumar: "))
num2 = int(input("Ingrese el segundo numero a sumar: "))
resultadoSuma = sumar(num1,num2)
print("El resultado de la suma es: {}".format(resultadoSuma))
