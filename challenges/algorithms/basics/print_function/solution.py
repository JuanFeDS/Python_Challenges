# Desafío de HackerRank:
# Descripción: 
# El código lee un número entero. Sin utilizar ningún método de cadena, intente imprimir lo siguiente:
# - 1234....n
# Donde ... representan los valores consecutivos en el medio

def print_function(n):
    '''
    Construye una cadena numérica sobre una iteración determinada.

    Args:
        n: Número entero
    
    Return:
        Retorna una cadena numérica
    '''

    mensaje = ''

    # Iteramos sobre la cantidad de veces indicadas
    for i in range(n):
        mensaje = mensaje + str(i+1)
    
    print(int(mensaje))

if __name__ == '__main__':
    # Ejemplo 1
    # Ejemplo 1
    number = int(input('Introduce un número: '))

    print_function(number)