# 'Desafío de CodeWars: Disemvowel Trolls
# Descripción: 
# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
import re

def disemvowel(string_):
    '''
    Elimina las vocales de una cadena de caracteres
    
    Arg
        string_: str Cadena de caracteres
    Return
        string_: str Retorna la cadena de caracteres sin vocales
    '''

    # Eliminamos las vocales con expresiones regulares
    string_ = re.sub(r'[aeiouAEIOU]', '', string_)

    return string_

if __name__ == '__main__':
    new_string = disemvowel('Hola')
    print(new_string)