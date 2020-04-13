<<<<<<< HEAD

class LRUcache():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        key = str(key)
        try:
            val = self.cache.pop(key)
        except:
            return -1
        self.cache[key] = val
        return val

    def put(self, key, value):
        key = str(key)
        self.cache.pop(key, None)
        if len(self.cache) >= self.capacity:
            popitem = next(iter(self.cache))
            print("LRU:", popitem)
            del self.cache[popitem]
        self.cache[key] = value

    def get_cache(self):
=======

class LRUcache():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        key = str(key)
        try:
            val = self.cache.pop(key)
        except:
            return -1
        self.cache[key] = val
        return val

    def put(self, key, value):
        key = str(key)
        self.cache.pop(key, None)
        if len(self.cache) >= self.capacity:
            popitem = next(iter(self.cache))
            print("LRU:", popitem)
            del self.cache[popitem]
        self.cache[key] = value

    def get_cache(self):
>>>>>>> 9fcb85a4b98d015a536757c1d127551f5639d91f
        print(self.cache)