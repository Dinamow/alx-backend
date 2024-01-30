#!/usr/bin/python3
"""lifo cache system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache class.

    This class represents a Last-In-First-Out (LIFO) cache implementation.
    It inherits from the BaseCaching class.

    Attributes:
        None

    Methods:
        __init__: Initialize the LIFOCache object.
        put: Add an item to the cache.
        get: Get an item from the cache by key.
        
        put: Add an item to the cache.
        
        get: Get an item from the cache by key.
    """
    
    def __init__(self):
        """Initialize the LIFOCache object.
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last))
            del self.cache_data[last]
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
