# from lru import *
from LRUcache import *
from time import sleep


def output(cache):
    for i,data in enumerate(cache.storage):
        print("index: {0} "
              "key: {1} "
              "data: {2} ".format(i,data.key,data.value))

print("Initial items")
cache = LRUCache(3)
cache.put(LRUnode(1,'1'))
cache.put(LRUnode(2,'2'))
cache.put(LRUnode(3,'3'))
output(cache)
print("\n")

print("Insert an existing item")
cache.put(LRUnode(1,'1'))
output(cache)
print("\n")