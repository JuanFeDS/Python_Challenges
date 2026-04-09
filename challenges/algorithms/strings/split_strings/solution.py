# 'Desafío de CodeWars: Split Strings

# Descripción: 
# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

import re

def solution(s):
    '''
    Divide los elementos del string en parejas
    
    Args:
        s(str): String que sera procesado.
    Return:
        elements(list): Retorna una lista con los elementos de dos en dos.
    '''
    
    # Evaluamos la longitud del string para determinar el flujo a seguir     
    if len(s) % 2 == 0:
        elements = re.findall(r'.{2}', s)
    else:
        # Si la cantidad de elementos es impar entonces agregamos "_"         
        s = f'{s}_'
        elements = re.findall(r'.{2}', s)

    return elements

if __name__ == '__main__':
    new_string = input('Introduce tu texto: ')
    
    elements = solution(new_string)
    print(elements)