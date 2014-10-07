'''
Created on 15/04/2013

@author: Alejandro
'''
import random
def deterministicNumber():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    return 10

def deterministicNumberlist():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    even_list=[10,12,14,16,18,20]
    return random.choice(even_list)

#print deterministicNumber()

def stochasticNumber():
    '''
    Stochastically generates a uniformly distributed even number between 9 and 21
    '''
    n= random.randint(9,21)
    while(n%2!=0):
        n= random.randint(9,21)
    return n

print stochasticNumber()