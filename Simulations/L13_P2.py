'''
Created on 15/04/2013

@author: Alejandro
'''
import random
def genEven():
    '''
    Generates a random even number x, where 0 <= x < 100
    '''
    #0 <= x < 100
    n= random.randint(0,99)
    print n
    while(n%2!=0):
        n= random.randint(0,99)
        print n
    return n

a= genEven()
print a