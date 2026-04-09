def first_non_repeating_character(s: str) -> str:
    """
    Encuentra el primer carácter no repetido en una cadena.

    Args:
    - s (str): Cadena de entrada en la que se buscará el primer carácter no repetido.

    Returns:
    - str: El primer carácter no repetido encontrado. Si no se encuentra ningún carácter no repetido, devuelve una cadena vacía.
    """

    # Convertir la cadena a minúsculas para manejar la insensibilidad a mayúsculas
    s_lower = s.lower()

    # Crear un diccionario para almacenar el recuento de cada carácter en la cadena en minúsculas
    dict_count = {caracter: s_lower.count(caracter) for caracter in s_lower}

    # Encontrar todos los caracteres únicos con un recuento de 1
    caracteres_unicos = [caracter for caracter in s if dict_count[caracter.lower()] == 1]

    # Obtener el primer carácter único, o devolver una cadena vacía si no se encuentra ningún carácter único
    try:
        primer_caracter = caracteres_unicos[0]
    except IndexError:
        primer_caracter = ""

    return primer_caracter


if __name__ == "__main__":
    print(first_non_repeating_character("sTreSS"))