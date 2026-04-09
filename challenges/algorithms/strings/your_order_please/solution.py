"""
Your task is to sort a given string. Each word in the string will contain a 
single number. This number is the position the word should have in the result.
"""

import re

def order(sentence: str) -> str:
    """Function to sort a text string by the numbers it contains.

    Args:
        sentence (str): The string to sort

    Returns:
        str: The string sorted
    """

    # We create a list with our string
    sentence_list = sentence.split()

    # We sorted the elements by the number that contain
    ordened_list = sorted(
        sentence_list, 
        key=lambda item: int(re.findall(r'\d+', item)[0])
    )
    
    # We return the ordened string
    return ' '.join(ordened_list)