class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}
        self.times = 0
    
    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.times
            self.times+=1
            return self.cache[key]
        return -1
    
    def put(self, key, val):
        if len(self.cache) >= self.capacity:
            lru_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(lru_key)
            self.lru.pop(lru_key)
        self.cache[key] = val
        self.lru[key] = self.times
        self.times+=1

