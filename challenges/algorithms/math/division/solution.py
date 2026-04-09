# Desafío de HackerRank: Division
# Descripción: 
# El código lee dos enteros *a* y *b*. Se deben imprimir 2 líneas donde:

# - La primera línea contiene la división de a sobre b redondeado.
# - La segunda línea contiene la división de b sobre a sin redondear.

def division(a, b):
    '''
    Calculo de operaciones divisiones

    Args:
        a: Número entero
        b: Número entero

    Return:
        Indica el resultado de las divisiones
    '''

    # Realizamos la división redondeando
    print(a//b)

    # Realizamos la división sin redondear
    print(a/b)


if __name__ == '__main__':

    # Ejemplo 1
    number_1 = int(input('Introduce el número a: '))
    number_2 = int(input('Introduce el número b: '))

    division(number_1, number_2)