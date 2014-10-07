'''
Created on 31/03/2013

@author: Alejandro
'''
class Queue(object):
    
        def __init__(self):
            """initialize your Queue"""
            self.vals = []
            
        def insert(self,e):
            "inserts one element in your Queue"
            self.vals.append(e)
            
        def remove(self):
            "removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError."
            if(len(self.vals)==0):
                raise ValueError("The queue is empty")
            else:
                self.vals.pop([0])