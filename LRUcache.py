class LRUnode():
    def __init__(self,key,value):
        self.key = key
        self.value = value


class LRUcache():
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int):
        key = str(key)
        try:
            val = self.cache.pop(key)
        except:
            return -1
        self.cache[key] = val        
        return val
    

    def put(self, key: int, value: int):
        key = str(key)
        self.cache.pop(key, None)
        if len(self.cache) >= self.capacity:
            pop_this = next(iter(self.cache))
            del self.cache[pop_this]
        self.cache[key]=value