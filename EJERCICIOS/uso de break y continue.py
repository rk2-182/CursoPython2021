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



