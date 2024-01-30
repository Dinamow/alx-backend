#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """this is a basic caching system class"""
    
    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
