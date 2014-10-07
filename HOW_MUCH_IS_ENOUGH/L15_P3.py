'''
Created on 22/04/2013

@author: Alejandro
'''
#from L15_2_HOW_MUCH_IS_ENOUGH import *
#import l15_2.py    #WRONG FORMAT    
#from l15_2 import * #OK
#from l15_2 import * #OK
from L15_2_HOW_MUCH_IS_ENOUGH.l15_2 import stdDev

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    standDev=0
    sumStr=0
    tot = 0.0
    if(len(L)==0):
        standDev=float('NaN') 
    else:
        
        for w in L:
            sumStr+=len(w)
        mean = sumStr/float(len(L))
        
        for w in L:
            tot += (len(w) - mean)**2
        
        standDev= (tot/len(L))**0.5
     
    return standDev

"""
TEST Section

['a', 'z', 'p']
0.0

['apples', 'oranges', 'kiwis', 'pineapples']
1.87082869339
"""
#L = ['a', 'z', 'p']
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)


