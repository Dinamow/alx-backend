#!/usr/bin/python3
"""lfu cache system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class represents a Least Frequently Used (LFU) cache implementation.
    It inherits from the BaseCaching class.
    """

    def __init__(self):
        """
        Initializes an instance of the LFUCache class.
        """
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """
        Adds an item to the cache with the given key.
        If the cache is full, it removes the least frequently used item(s) before adding the new item.

        Args:
            key: The key of the item to be added.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_count = min(self.count.values())
            min_keys = [k for k in self.count if self.count[k] == min_count]
            if len(min_keys) == 1:
                del self.cache_data[min_keys[0]]
                del self.count[min_keys[0]]
                print("DISCARD: {}".format(min_keys[0]))
            else:
                for k in self.cache_data:
                    if k in min_keys:
                        del self.cache_data[k]
                        del self.count[k]
                        print("DISCARD: {}".format(k))
                        break
        self.cache_data[key] = item
        self.count[key] = 0

    def get(self, key):
        """
        Retrieves the item associated with the given key from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the given key, or None if the key is not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.count[key] += 1
        return self.cache_data[key]
