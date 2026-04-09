# Desafío de CodeWars: Linear Regression of Y on X
# Descripción: Se debe crear una función que calcule el valor de la pendiente y el intercepto de una regresión lineal dado un conjunto de datos 

import numpy as np

def regression_line(x, y):
    """ 
    Calculo de la pendiente e intercepto para un conjunto de datos
    
    Args
        x: lista de valores de la variable dependiente
        y: lista de valores de la variable independiente
    
    Return
        tuple: Pendiente e Intercepto
    
    """
    # Convertimos nuestras listas en array para realizar operaciones
    x = np.array(x)
    y = np.array(y)

    # Definimos las variables que serviran para calcular nuestras incongnitas     
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_x_y = np.sum(x*y)

    # Aplicamos la formula para la pendiente y redondeamos a 4 digitos     
    a = round(
        ((sum_x_squared * sum_y) - (sum_x * sum_x_y)) / ((n * sum_x_squared) - sum_x**2),
        4)

    # Aplicamos la formula para el intercepto y redondeamos a 4 digitos     
    b = round(
        ((n * sum_x_y) - (sum_x * sum_y)) / ((n * sum_x_squared) - (sum_x**2)),
        4)

    # Retomamos la pendiente y el intercepto     
    return (a, b)

if __name__ == '__main__':
    # Ejemplo 1

    x1 = [25,30,35,40,45,50]
    y1 = [78,70,65,58,48,42]
    # Los valores a retornar son (114.381, -1.4457)
    
    pendiente, intercepto = regression_line(x1, y1)
    print(pendiente, intercepto)