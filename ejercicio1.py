import sys
from ast import main
print('EJERCICIO 1')

def dividir(a,b):
    #Utilizamos try y except para controlar las excepciones

    try:
        a/b #Realizamos la operación

    except ZeroDivisionError: #En el caso de que b=0 se ejecutará la excepción ya que sería un error del tipo ZeroDivisonError
        print('No es posoble dividir entre cero.') #cuando el denominador sea 0, el programa lanzará este mensaje.
