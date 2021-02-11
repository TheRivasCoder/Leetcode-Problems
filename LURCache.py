# Requires OrderedDict to keep track of most recently accessed Key Value pair
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int): # constructer requires capacity to limit the number of items in Cache
        self.capacity = capacity
        self.dictionary = OrderedDict()
        
    def get(self, key: int) -> int: # Get function return value for specific key and moves item to end of dictionary as most recently accessed
        if key in self.dictionary:
            self.dictionary.move_to_end(key)
            return self.dictionary[key]
        return -1

    def put(self, key: int, value: int) -> None: # Put function adds item to dictionary and removes least recent item from dictionary if number of items is over capacity
        if key in self.dictionary:
            self.dictionary.move_to_end(key) # moves item to end of dictionary if it already exists in dictionary
        self.dictionary[key] = value 
        if self.capacity < len(self.dictionary):
            self.dictionary.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

myCache = LRUCache(4)
myCache.put(3,30)
myCache.put(4,40)
print(myCache.get(3))
print(myCache.dictionary)