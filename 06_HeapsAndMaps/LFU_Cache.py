#!/usr/bin/env python3
import sys
from collections import OrderedDict
import collections

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class LFUCache:
    def __init__(self, capacity: int):
        self.freq = {}
        self.cache = {} 
        self.capacity = capacity
        self.min = 1       

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache[key] += 1
        count = self.cache[key]
        if count not in self.freq:
            self.freq[count] = collections.OrderedDict()
        value = self.freq[count-1][key]
        self.freq[count][key] = value
        del self.freq[count-1][key]            
        return value
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return     
        if len(self.cache) >= self.capacity and key not in self.cache:
            while self.min not in self.freq or len(self.freq[self.min]) == 0: self.min += 1
            temp, val = self.freq[self.min].popitem(last = False)
            del self.cache[temp]
            
        if key not in self.cache:
            self.min = 1
            self.cache[key]  = 1
            if 1 not in self.freq:
                self.freq[1] = collections.OrderedDict()
            self.freq[1][key] = value
        else:
            count = self.cache[key]
            self.cache[key] = count + 1
            if count + 1 not in self.freq:
                self.freq[count+1] = collections.OrderedDict()
            self.freq[count+1][key] = value
            del self.freq[count][key]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    cache_max_size = 4
    cache_size = 0
    s = LFUCache(cache_max_size)
    s.put(1, 10)
    s.put(2, 20)
    print(s.get(1))
    s.put(3, 30)
    print(s.get(2))
    s.put(4, 40)
    s.put(5, 50)

    print(s.freq)
    print(s.cache)