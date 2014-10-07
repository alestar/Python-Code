'''
Created on 31/03/2013

@author: Alejandro
'''
def isPrime(n):
    """
    Returns True if the positive integer n is prime, and False otherwise.  
    
    Raises a TypeError if n isn't an integer.
    Raises a ValueError if n is an integer less than or equal to zero.
    """
    # Check if n is an integer, if not, raise a TypeError
    if type(n) != int:
        raise TypeError()
    # Check if n is negative; if so, raise a ValueError
    if n <= 0:
        raise ValueError()

    # Otherwise, check if n is prime!
    # Actually we only need to test divisors up to sqrt(n) -- this optimization
    #  makes the code run faster
    if n == 2:
        return True
    elif n < 2:
        return False
    for divisor in range(2, int(n**0.5+1)):
        if n % divisor == 0: 
            return False

    return True