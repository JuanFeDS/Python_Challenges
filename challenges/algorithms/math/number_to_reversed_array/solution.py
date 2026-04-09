"""
Given a random non-negative number, you have to return the digits
of this number within an array in reverse order.
"""

def digitize(n: int) -> list:
    """_summary_

    Args:
        n (int): number to reverse.

    Returns:
        list: List of digits reversed
    """
    return [int(digit) for digit in str(n)][::-1]
