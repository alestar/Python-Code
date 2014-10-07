'''
Created on 15/04/2013

@author: Alejandro
'''
import random
random.seed(9001)
for i in xrange(random.randint(1, 10)):
    print random.randint(1, 10)
    
random.seed(9001)
d = random.randint(1, 10)
for i in xrange(random.randint(1, 10)):
    print d