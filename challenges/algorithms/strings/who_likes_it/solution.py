# 'Desafío de CodeWars: Who likes it?
# Descripción: 

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

def likes(names):
    '''
    Determinar el mensaje a mostrar dependiendo de la cantidad de likes recibidos
    
    Args:
        names: Lista de personas que dieron like
    Return:
        Indica el mensaje a mostrar en función de un sistema de reglas
    
    '''

    # Calculamos el número de personas que dieron like         
    num_likes = len(names)

    # Definimos  los mensajes a mostrar     
    templates = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }

    # Seleccionamos el mensaje dependiendo de la cantidad de usuarios 
    message = templates[min(4, num_likes)]
    
    # Ajustamos los campos de nombres     
    if num_likes < 4:
        return message.format(*names[:3])
    else:
        return message.format(*names[:2], others=(num_likes - 2))