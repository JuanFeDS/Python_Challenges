# Desafío de HackerRank: Arithmetic Operators
# Descripción: 
# El código lee dos enteros *a* y *b*. Se deben imprimir 3 líneas donde:

# - La primera contiene la suma de los dos números.
# - La segunda contiene la resta de los dos números.
# - La tercera contiene la multiplicación de los dos números.

def arithmetic_operators(a, b):
    '''
    Calculo de operaciones aritméticas

    Args:
        a: Número entero
        b: Número entero

    Return:
        Indica el resultado de las operaciónes matemáticas
    '''

    # Realizamos la suma
    print(a + b)

    # Realizamos la resta
    print(a - b)

    # Realizamos la multiplicación
    print(a * b)


if __name__ == '__main__':

    # Ejemplo 1
    number_1 = int(input('Introduce el número a: '))
    number_2 = int(input('Introduce el número b: '))

    arithmetic_operators(number_1, number_2)
