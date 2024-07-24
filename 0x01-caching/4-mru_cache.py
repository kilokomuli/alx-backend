#!/usr/bin/env python3
"""Implement MRU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Class MRUCache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None or item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recent_key = next(reversed(self.cache_data))
                del self.cache_data[most_recent_key]
                print("DISCARD:", most_recent_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)