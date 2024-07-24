#!/usr/bin/env python3
"""LRU Caching module"""
from base_caching import BaseCaching
from collections import OrderedDict  


class LRUCache(BaseCaching):
    """ Defines LRU Caching class"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item at the end of the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", lru)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key"""
        return self.cache_data.get(key, None)