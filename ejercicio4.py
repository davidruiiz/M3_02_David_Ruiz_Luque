from ast import main
import sys

print('\nEJERCICIO 4\n')

def suma(a,b):
    try:
        return a+b
    except TypeError: 
        return '\nOperación no válida.'
        
