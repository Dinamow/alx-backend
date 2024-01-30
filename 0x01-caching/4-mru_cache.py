#!/usr/bin/python3
"""mru cache system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU cache class.

    This class represents a Most-Recently-Used (MRU) cache implementation.
    It inherits from the BaseCaching class.

    Attributes:
        MAX_ITEMS (int):
            The maximum number of items that the cache can hold.
        cache_data (dict):
            A dictionary to store the key-value pairs of the cache.
        __last (list):
            A list to keep track of the most recently used keys in the cache.

    Methods:

        __init__: Initialize the MRUCache object.
        put: Add an item to the cache.
        get: Get an item from the cache by key.
    """

    def __init__(self):
        """
        Initializes the LRU Cache object.
        """
        super().__init__()
        self.__last = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, the least recently used item will be discarded.

        Args:
            key: The key of the item to be added.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            last = self.__last.pop(-1)
            if key not in self.cache_data:
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
        self.__last.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        If the item is not in the cache, None will be returned.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the key,
            or None if the key is not in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.__last.append(self.__last.pop(self.__last.index(key)))
        return self.cache_data.get(key)
