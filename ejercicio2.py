from ast import main
import main

print('\nEJERCICIO 2\n')

lista=[4, 7, 30, 23, 5]

def imprimir_elemento_lista(lista, posicion):
    ##Utilizamos try y except para controlar las excepciones
    try:
        return lista[posicion] 
    except IndexError: #En caso de que el índice dado exceda la longitud de la lista, usamos IndexError para controlar la excepción
        return 'El índice está fuera del rango.' #cuando esto ocurra se lanzará este mensaje

#Ejemplo
print(imprimir_elemento_lista(lista, 11))

#Importamos a main
if __name__=="__main__":
    main()


