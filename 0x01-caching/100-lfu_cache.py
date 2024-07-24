#!/usr/bin/env python3
"""LFU Caching module"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """Defines class LFUCache
    Least Frequent Used"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq = defaultdict(int)
        self.freq_order = defaultdict(OrderedDict)
        self.min_freq = 0
    
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k, v = self.freq_order[self.min_freq].popitem(last=False)
            del self.cache_data[k]
            del self.freq[k]
            print("DISCARD:", k)
        self.cache_data[key] = item
        self.freq[key] = 1
        self.min_freq = 1
        self.freq_order[1][key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        freq = self.freq[key]
        del self.freq_order[freq][key]
        if not self.freq_order[freq]:
            if freq == self.min_freq:
                self.min_freq += 1
            del self.freq_order[freq]

        self.freq[key] += 1
        self.freq_order[self.freq[key]][key] = item

        return item        
