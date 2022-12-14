import sys
from ast import main

print('EJERCICIO 1\n')

def dividir(a,b):
    #Utilizamos try y except para controlar las excepciones
    try:
        return a/b  #Realizamos la operación

    except ZeroDivisionError: #En el caso de que b=0 se ejecutará la excepción ya que sería un error del tipo ZeroDivisonError
        print('No es posoble dividir entre cero.') #cuando el denominador sea 0, el programa lanzará este mensaje.
        return 'Operación no válida.'
        sys.exit()
    

#Ejemplo

print(dividir(7, 0))

#Importamos a main
if __name__ == "__main__":  
    main()