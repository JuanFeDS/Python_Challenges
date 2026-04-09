def distances_from_average(test_list: list) -> list:
    '''
    Calcula la distancia entre cada elemento de la lista y su promedio

    Args:
        test_list(list) -> Lista de valores iniciales
    Return:
        distance_list(list) -> Lista con las respectivas distancias
    '''    

    # Calculamos el promedio
    mean = sum(test_list) / len(test_list)

    # Evaluamos la distancia para cada elemento     
    distance_list = [round(mean - i, 2) for i in test_list]

    return distance_list

if __name__ == '__main__':
    input_list = [55, 95, 62, 36, 48]

    distances_from_average(input_list)