"""
Create a function that takes an integer as an argument and returns "Even" 
for even numbers or "Odd" for odd numbers.
""" 

def even_or_odd(number) -> str:
    """This function evaluates whether the number is even or odd.

    Args:
        number (int): The number to evaluate

    Returns:
        str: The type of number that is
    """
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'