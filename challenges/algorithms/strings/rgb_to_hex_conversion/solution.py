def rgb(r, g, b):
    """
    Convierte un color RGB a su representación hexadecimal.

    Args:
    r (int): Valor del canal rojo (0-255).
    g (int): Valor del canal verde (0-255).
    b (int): Valor del canal azul (0-255).

    Returns:
    str: Representación hexadecimal del color.
    """
    # Asegurar que los valores RGB estén en el rango válido (0-255)
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Convertir cada valor RGB a hexadecimal
    hex_r = format(r, '02X')
    hex_g = format(g, '02X')
    hex_b = format(b, '02X')

    # Combinar los valores hexadecimales para formar el color completo
    hex_color = hex_r + hex_g + hex_b

    return hex_color

if __name__ == '__main__':
    print(rgb(-20, 275, 125))