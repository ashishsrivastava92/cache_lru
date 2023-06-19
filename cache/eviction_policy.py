from abc import ABC, abstractmethod

from data_structure import DoublyLinkedList, DLLNode


class EvictionPolicy(ABC):
    # inheritance base class

    @abstractmethod
    def key_access(self, key):
        pass

    @abstractmethod
    def evict_key(self):
        pass


class LRUEviction(EvictionPolicy):
    # LRU class
    # Use DLL and map implementation

    def __init__(self):
        self.node_map = dict()
        self.dll = DoublyLinkedList()

    def key_access(self, key, value=None):
        # detach node - N
        if key in self.node_map:
            node = self.dll.detach_node(self.node_map[key])
            # Add N at tail
            self.dll.add_node_at_last(node)
        self.node_map[key] = DLLNode(value)
        self.dll.add_node_at_last(self.node_map[key])
        return

    def evict_key(self):
        # get first node and detach
        node = self.dll.get_first_node()
        self.dll.detach_node(node)
        return node
