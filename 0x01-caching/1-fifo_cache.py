#!/usr/bin/env python3
"""FIFO Cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines and implements FIFO caching system
    """
    def __init__(self):
        """Initializes the FIFO caching system"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
                self.cache_data[key] = item
                if key not in self.queue:
                    self.queue.append(key)

    def get(self, key):
        """Gets an item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)