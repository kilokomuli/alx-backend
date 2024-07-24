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
        if key is None and item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last = self.cache_data.popitem(True)
                print("DISCARD: {}".format(last))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Gets an item by key"""
        return self.cache_data.get(key, None)
