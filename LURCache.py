from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.dictionary:
            self.dictionary.move_to_end(key)
            return self.dictionary[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.move_to_end(key)
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