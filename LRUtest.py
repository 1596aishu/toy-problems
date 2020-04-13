# from lru import *
from LRUcache import *
from time import sleep


print("Initial items")
caches = LRUcache(3)
caches.put(1,'one')
caches.put(2,'two')
caches.put(3,'three')
caches.get_cache()
print("\n")

print("Insert an existing item")
caches.put(1,'one')
caches.get_cache()
print("\n")

print("Insert an existing item")
caches.put(2,'two')
caches.get_cache()
print("\n")

print("Insert an new item")
caches.put(6,'six')
caches.get_cache()
print("\n")

print("Insert an existing item")
caches.put(2,'two_modified')
caches.get_cache()
print("\n")

print("Insert an existing item")
caches.put(1,'one_modified')
caches.get_cache()
print("\n")

print("Insert an new item")
caches.put(3,'three')
caches.get_cache()
print("\n")