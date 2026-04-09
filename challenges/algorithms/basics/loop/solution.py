# Desafío de HackerRank:
# Descripción: 
# El código toma un entero e itera la cantidad de veces correspondientes a su valor. 
# Por cada iteración imprime el valor del número al cuadrado

def loop(n):
    '''
    Itera una cantidad determinada de veces y en cada iteración imprime el valor del número al cuadrado
    Args:
        n: Número entero
    '''

    # Iteramos sobre la cantidad determinada
    for i in range(n):
        print(i**2)

if __name__ == '__main__':
    # Ejemplo 1
    number = int(input('Introduce el número: '))

    loop(number)