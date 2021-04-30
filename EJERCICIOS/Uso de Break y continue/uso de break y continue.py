################break y continue####################

n = 1

"""
while n < 11:
    r = 5*n
    print("5 X {} = {}".format(n,r))
    n=n+1
"""

"""
#break
while n < 11:
    r = 5*n
    print("5 X {} = {}".format(n,r))

    # si n es igual a 5 terminar ciclo
    if n == 5:
        break
    n=n+1
"""

#continue
while n < 11:
    r = 5*n
    print("5 X {} = {}".format(n,r))

    # si n es igual a 5 el ciclo se devuele al ciclo y no ejecuta la instruccion
    if n == 5:
        continue
    
    n=n+1

##############Ejercicio 2 ############################
"""
Pedir al usuario que ingrese una palabra.
Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separad
"""
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.

userWord = input("ingresa una palabra: ")

userWord = userWord.upper()
for letra in userWord:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    print(letra)
    



