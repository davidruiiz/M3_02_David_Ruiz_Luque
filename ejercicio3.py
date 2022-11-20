from ast import main
import sys

print('\nEJERCICIO 3\n')

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" }

def imprimir_clave_valor(lista, pais):
    ##Utilizamos try y except para controlar las excepciones
    try:
        return lista[pais] #Se accede al valor de una clave dada

    except KeyError: #En el caso de no encontrar el valor, usamos KeyError para controlar la excepción
        return 'Valor no encontrado.' #En ese caso, el programa lanzará este mensaje
        sys.exit()




