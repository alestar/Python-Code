'''
Created on 22/04/2013

@author: Alejandro


The coefficient of variation is the standard deviation divided by the mean.
Loosely, it's a measure of how variable the population is in relation to the mean.
coefficient of variation
'''
def cofcVar(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    stanDev=(tot/len(X))**0.5
    return  stanDev/mean

"""
TEST Section
"""
L=  [10, 4, 12, 15, 20, 5] 

print cofcVar(L)