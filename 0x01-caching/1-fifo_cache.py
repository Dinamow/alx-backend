#!/usr/bin/python3
"""fifo cache system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo chache class

    Args:
        BaseCaching (class): [base caching class]
    """

    def __init__(self):
        """initializer"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            if key not in self.cache_data:
                print("DISCARD: {}".format(first))
                del self.cache_data[first]
        self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
