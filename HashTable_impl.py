# -*- coding: utf-8 -*-
"""
Hash Table/Map implementation

@author: pram
"""

class HashTable:
    
    def __init__(self):
        self.MAX=10
        self.arr= [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h=0
        for char in key:
            h+= ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h=self.get_hash(key)
        self.arr[h] = val
        
    def rem(self,key):
        h=self.get_hash(key)
        self.arr[h]=None
        
    
    
