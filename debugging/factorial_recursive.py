#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given non-negative integer using recursion.
    
    Parameters:
    n (int): The number for which the factorial is to be calculated.
    
    Returns:
    int: The computed factorial of the number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Pass the first command-line argument to the function and print the result
f = factorial(int(sys.argv[1]))
print(f)
