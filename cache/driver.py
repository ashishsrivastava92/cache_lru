
from cache import CacheFactory

if __name__ == "__main__":
    cache = CacheFactory.create_cache(cache_type="Default")
    print(cache.__dict__)
    print(cache.get(5))
    cache.put(5, "hello")
    cache.put(6, "world")
    print(cache.get(5))
    (cache.__dict__)

