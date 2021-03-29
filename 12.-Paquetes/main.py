""" 
    Archivo principal para probar los modulos
"""

#utilizar modulos del paquete
from miPaquete import login

user = input("User: ")
password = int(input("Password:"))

login.login(user,password)