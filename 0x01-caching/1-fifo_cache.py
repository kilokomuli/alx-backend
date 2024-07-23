#!/usr/bin/env python3
"""FIFO Cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Defines and implements FIFO caching system
    """
    def __init__(self):
        """Initializes the FIFO caching system"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Gets an item from cache"""
        return self.cache_data.get(key, None)