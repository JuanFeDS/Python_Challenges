def hashtag_generator(text):
    '''
    Genera hashtags segun las reglas definidas
    Args:
        text(str): Texto original
    Return:
        hastag(str): Texo en el formato del hashtag
    '''
    
    # Creamos una lista apartir del texto original     
    text_in_list = text.split(' ')
    
    # Capitalizamos cada uno de los elementos de la lista     
    text_in_list = [i.capitalize() for i in text_in_list]
    
    # Combinamos el contenido de nuestra lista en un solo string        
    hashgtag = ''.join(text_in_list)

    # Aplicamos las reglas definidas     
    if len(hashgtag) + 1 > 140:
        return False
    elif len(hashgtag) == 0:
        return False
    else:
        return (f'#{hashgtag}')


if __name__ == '__main__':
    new_string = input('Introduce tu texto: ')

    hashtag = hashtag_generator(new_string)
    print(hashtag)