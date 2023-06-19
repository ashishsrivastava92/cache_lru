
class DLLNode:
    # Doubly L-List Node

    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None

    def get_element(self):
        return self.element


class DoublyLinkedList:
    # Doubly L-List implementation
    def __init__(self):
        self.head = DLLNode(None)
        self.tail = DLLNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    @staticmethod
    def detach_node(node):
        if node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        return node

    def add_node_at_last(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        self.tail.prev = node
        node.next = self.tail

    def is_empty(self):
        if self.head.next != self.tail:
            return False

    def get_first_node(self):
        # get head.next
        return self.head.next

    def get_last_node(self):
        # get tail.prev
        return self.tail.prev
