#!/usr/bin/python3
"""
1. FIFO caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        method initializer/constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        Method that add key:value to the dictionary self.cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                    print("DISCARD: {}".format(next(iter(self.cache_data))))
                    del self.cache_data[next(iter(self.cache_data))]
                self.cache_data[key] = item

    def get(self, key):
        """
        Method that return the value of dict self.cahce_data linked to key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
