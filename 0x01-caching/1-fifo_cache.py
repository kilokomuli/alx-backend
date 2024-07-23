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

        """Gets an item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
