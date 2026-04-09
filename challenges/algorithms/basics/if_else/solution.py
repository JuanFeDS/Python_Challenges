# 'Desafío de HackerRank: Python If-Else

# Descripción: Determinar números 'Weird' o 'Not Weird'
# Dado un entero, *n*, realiza las siguientes acciones condicionales:

# - Si *n* es impar, imprime *"Weird"*
# - Si *n* es par y esta en el rango inclusivo de **2** y **5**, imprime *"Not Weird"*
# - Si *n* es par y esta en el rango inclusivo de **6** y **20**, imprime *"Weird"*
# - Si *n* es par y est mayor que **20**, imprime *"Not Weird"*

def if_else(n):
    """ 
    Determinar si un número es 'Weird' o 'Not Weird' dado un conjunto de reglas
    
    Args
        n: Número entero
    
    Return
        Indica si el número es 'Weird' o 'Not Weird'
    """

    # Definimos la lógica condicional para cada regla
    if n%2 != 0:
        print('Weird')
    elif n%2 == 0 and n>=2 and n<=5:
        print('Not Weird')
    elif n%2 == 0 and n>=6 and n<=20:
        print('Weird')
    elif n%2 == 0 and n>20:
        print('Not Weird')

if __name__ == '__main__':
    # Ejemplo 1
    number = int(input('Introduce un número: '))

    if_else(number)