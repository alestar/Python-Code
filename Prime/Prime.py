'''
Created on 31/03/2013

@author: Alejandro
'''
from IPython.utils.traitlets import Int
def isPrime(n):
    prime=True
    if type(n) != int:
        raise TypeError()
        prime=False
    if n <= 0:
        raise ValueError()
        prime=False 
    
    for i in range(2,n-1):
        if (n%i==0):
            prime=False
            break        
    
    return prime

# print isPrime("6")
print isPrime(2)
# print isPrime(5.54)
#print isPrime([1,2,3])
# print isPrime(-1)
# print isPrime(0)