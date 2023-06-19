from abc import ABC, abstractmethod

from exceptions import OverflowException, KeyNotFound


class Storage(ABC):
    # inheritance class for storage type

    @abstractmethod
    def add(self, key, value):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass


class MapInMemoryStorage(Storage):
    # In memory map implementation

    def __init__(self, capacity=10):
        self.map = dict()
        self.capacity = capacity
        self.current_data = 0

    def add(self, key, value):
        if self.capacity == self.current_data:
            # Overflow case
            raise OverflowException
        self.map[key] = value
        self.current_data += 1
        return self.map[key]

    def remove(self, key):
        if key in self.map:
            del self.map[key]
            self.current_data -= 1
            return
        raise KeyNotFound

    def get(self, key):
        return self.map.get(key, None)
