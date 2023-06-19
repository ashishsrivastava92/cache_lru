from eviction_policy import LRUEviction
from storage import MapInMemoryStorage
from exceptions import *


class DefaultCache:
    # Default cache

    def __init__(self):
        print("initializing...")
        self.eviction_policy = LRUEviction()
        self.storage = MapInMemoryStorage()

    def put(self, key, val):
        # Push data in storage
        try:
            self.storage.add(key, val)  # raise exception: Capacity overflow
            # Run eviction policy
            self.eviction_policy.key_access(key)
        except (KeyNotFound, OverflowException):
            key_to_remove = self.eviction_policy.evict_key()
            if not key_to_remove:
                print("unexpected stage: Storage full, no key to remove")
            self.storage.remove(key_to_remove)
            self.put(key, val)

    def get(self, key):
        # Get Data from storage
        value = self.storage.get(key)
        if not value:
            print("Access for key not existing")
            return None
        self.eviction_policy.key_access(key)
        return value


class CacheFactory:
    # Cache Factory

    def create_cache(cache_type=None):
        if not cache_type or cache_type == "Default":
            print("Building default cache")
            cache_obj = DefaultCache()
            print(cache_obj.__dict__)
            return cache_obj
