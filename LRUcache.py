from datetime import datetime

class LRUnode():
    def __init__(self,key,value):
        self.key = key
        self.value = value


class LRUcache():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.storage = []
        

    def get(self, key):
        if key in self.cache:
            self.storage.remove(key)
            self.storage.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.storage.remove(key)
            self.storage.append(key)
            self.cache[key] = value
        else:
            if len(self.storage) < self.capacity:
                self.storage.append(key)
                self.cache[key] = value
            else:
                del self.cache[self.storage[0]]
                self.storage.pop(0)
                self.cache[key] = value
                self.storage.append(key)