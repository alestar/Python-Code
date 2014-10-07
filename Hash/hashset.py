'''
Created on 01/04/2013

@author: usuario
'''
class hashset(object):
    
    def __init__(self, numBuckets): 
        '''
        numBuckets: int. The number of buckets this hash set will have. 
        Raises ValueError if this value is not an integer, or if it is not greater than zero.
    
        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if(type(numBuckets)!= int):
            raise ValueError
        else:
            self.numBuckets = numBuckets
            self.hashset= []
            for i in range(numBuckets):
                bucket=[]
                self.hashset.append(bucket)
               
    def hashValue(self, e):
        '''
        e: an integer
    
        returns: a hash value for e, which is simply e modulo the number of 
         buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if(type(e)!= int):
            raise ValueError
        else:
            return e % self.numBuckets
    
    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        if(type(e)!= int):
            raise ValueError
        else:
            for i in range(self.numBuckets):
                bucket= hashset[i]
                if e in bucket:
                    return True
                    break
        return False
        
    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        ''' 
        hashvalue= self.hashValue(e)
        if not (e in self.hashset[hashvalue]):
            self.hashset[hashvalue]= e
        
    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        bucket=[]
        if(type(e)!= int):
            raise ValueError
        if not (self.member(e)):
            raise ValueError
        else:
            for i in range(self.numBuckets):
                bucket= hashset[i]
                if e in bucket:
                    bucket.pop(e)
            
    def getNumBuckets(self):
        """
        Return an integer the number of buckets
        """
        return len(self.hashset)
    
    def __str__(self):
        """
        Return an integer the number of buckets
        good way to represent the hashSet's data.
        """
        resul=""
        bucket=[]       
        for i in range(self.numBuckets):
            bucket= hashset[i]
            resul+= str(i) +" "
        self.bucket.sort()
        resul+= '{' + ','.join([str(e) for e in self.bucket]) + '}'
        
        return resul