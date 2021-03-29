""" Modulo: Un módulo le permite a usted organizar lógicamente su código Python. Agrupando código relacionado dentro de un módulo hace el código mas fácil de entender y usar. Un módulo es un objeto de Python con atributos con nombres arbitrarios que puede enlazar y hacer referencia.
    Simplemente, un módulo es no es otra cosa sino un archivo con extensión .py. Un módulo puede definir funciones, clases y variables, también puede incluir código ejecutable.
    fuente: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion8/modulos.html#:~:text=Un%20m%C3%B3dulo%20es%20un%20objeto,tambi%C3%A9n%20puede%20incluir%20c%C3%B3digo%20ejecutable."""


# importar todos los modulos y dejar un alias
import calculadora as cal


print("**********Calculadora 1.0***********\n")
print("Menu")
print("1.-Sumar")
print("2.-Restar")
print("3.-Multiplicar")
print("4.-Dividir")

try:
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        print("Sumar")
        print("----------")
        num1 = int(input("Ingrese el primer numero a sumar: "))
        num2 = int(input("Ingrese el segundo numero a sumar: "))
        resultadoSuma = cal.sumar(num1,num2)
        print("El resultado de la suma es: {}".format(resultadoSuma))
    elif opcion == 2:
        print("Restar")
        print("----------")
        num1 = int(input("Ingrese el primer numero a restar: "))
        num2 = int(input("Ingrese el segundo numero a restar: "))
        resultadoResta = cal.restar(num1,num2)
        print("El resultado de la resta es: {}".format(resultadoResta))

    elif opcion == 3:
        print("Multiplicar")
        num1 = int(input("Ingrese el primer numero a sumar: "))
        num2 = int(input("Ingrese el segundo numero a sumar: "))
        resultadoMultiplicacion = cal.multiplicar(num1,num2)
        print("El resultado de la multiplicación es: {}".format(resultadoMultiplicacion))
    elif opcion == 4:
        print("Dividir")
        num1 = int(input("Ingrese el primer numero a sumar: "))
        num2 = int(input("Ingrese el segundo numero a sumar: "))
        resultadoDividir = cal.dividir(num1,num2)
        print("El resultado de la división es: {}".format(resultadoDividir))
except ValueError:
    print("El valor ingresado no es correcto")
finally:
    print("Que tenga buen dia!")
