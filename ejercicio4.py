from ast import main
import sys

print('\nEJERCICIO 4\n')

def suma(a,b):
    try: #Utilizamos try y except para controlar las excepciones
        return a+b
    except TypeError: #En el caso de que uno de los dos números sea de tipo cadena o booleano saltará la excepción TypeError 
        print('No se puede concatenar un "string" con un "int".') #En tal caso el programa imprimirá este mensaje
        return '\nOperación no válida.'
        sys.exit()

#Ejemplo:
print(suma('3',5))

#Importamos a main

if __name__=='__main__':
    main()

