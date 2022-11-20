from ast import main
import sys

print('\nEJERCICIO 3\n')

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" }

def imprimir_clave_valor(paises, valor):
    #Utilizamos try y except para controlar las excepciones
    try:
        return paises[valor] #Se accede al valor de una clave dada

    except KeyError: #En el caso de no encontrar el valor, usamos KeyError para controlar la excepción
        print('Valor no encontrado.') #En ese caso, el programa lanzará este mensaje
        return 'Operación no válida.'
        sys.exit()

#Ejemplo
print(imprimir_clave_valor(paises, 'alemania'))

#Importamos a main

if __name__=='__main__':
    main()



