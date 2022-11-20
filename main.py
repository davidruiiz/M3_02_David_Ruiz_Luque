import sys
from ast import main
print('EJERCICIO 1')

def dividir(a,b):
    #Utilizamos try y except para controlar las excepciones

    try:
        a/b #Realizamos la operación

    except ZeroDivisionError:

           