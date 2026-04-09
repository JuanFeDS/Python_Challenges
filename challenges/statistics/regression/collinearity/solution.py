import numpy as np

def collinearity(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Verifica si dos vectores definidos por puntos (x1, y1) y (x2, y2) son colineales.

    Parámetros:
    x1, y1 : int
        Coordenadas del primer punto que define el primer vector.
    x2, y2 : int
        Coordenadas del segundo punto que define el segundo vector.

    Retorna:
    bool
        True si los vectores son colineales (linealmente dependientes), False en caso contrario.
    """

    # Creamos nuestros vectores 
    vector_1 = np.array([x1, y1])
    vector_2 = np.array([x2, y2])

    # Construimos nuestra matriz
    matrix = np.column_stack((vector_1, vector_2))
    
    determinante = np.linalg.det(matrix)
    
    # Verificamos si el determinante es cero
    if determinante == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(collinearity(-15, 74, 105, -518))