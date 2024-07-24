#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Defines class LIFOCache that inherits from BaseCahing"""
    def __init__(self):
        """Initializes the class and calls the parent init"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                l_key = self.cache_data.popitem(True)
                print("DISCAR:", l_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Gets an item by key"""
        return self.cache_data.get(key, None)
