# Desafío de HackerRank:
# Descripción: 
# Casi cada cuatro años se añade un día extra al calendario, el 29 de febrero, y el día se denomina bisiesto. Corrige el calendario por el hecho de que nuestro planeta tarda aproximadamente 365,25 días en orbitar alrededor del sol. Un año bisiesto contiene un día bisiesto.

# En el calendario gregoriano se utilizan tres condiciones para identificar los años bisiestos:
# - El año se puede dividir uniformemente entre 4, es bisiesto, a menos que:
#   - El año se puede dividir uniformemente entre 100, NO es año bisiesto, a menos que:
#       - El año también es divisible por 400. Entonces es un año bisiesto.
# Esto significa que en el calendario gregoriano los años 2000 y 2400 son años bisiestos, mientras que 1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos. 

# Dado un año, determinar si es bisiesto. Si es un año bisiesto, devuelve el valor booleano Verdadero; en caso contrario, devuelve Falso.

def is_leap(year):
    '''
    Identifica si el año es bisiesto dado un conjunto de reglas
    
    Args
        year: Número entero

    Return: 
        Indica si el año es bisiesto o no
    '''
    
    leap = False

    # Definimos el sistema de reglas
    if year%4 == 0:
        if year%100 == 0:
            leap = False
            if year%400 == 0: 
                leap = True
        else:
            leap = True            
    
    print(leap)

if __name__ == '__main__':

    # Ejemplo 1
    number = int(input('Introduce un número: '))

    is_leap(number)