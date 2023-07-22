from collections import defaultdict
class Node:
    def __init__(self, value):
        self.value = value
        self._prev:Node = None
        self._next:Node = None
    
    def __repr__(self) -> str:
         return f"{self.value}"

class HashedLinkedList:
    def __init__(self, __iterable: None = None):
        self.head: Node = None
        self.tail: Node = None
        self.hashmap = defaultdict(list)
        if __iterable:
            for v in __iterable:
                node = Node(v)
                self.insert(node)

    def insert(self, node:Node):
        self.hashmap[node.value].append(node)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
             newNode = node
             newNode._next = self.head
             self.head._prev = newNode
             self.head=newNode

    def remove(self, value):
        if value in self.hashmap:
            nodes = self.hashmap[value]
            node: Node = nodes.pop()
            if len(nodes) == 0:
                del self.hashmap[value]

            if node == self.head:
                self.head = self.head._next
                if self.head:
                    self.head._prev = None
                else:
                    self.tail = None
            elif node == self.tail:
                self.tail = self.tail._prev
                if self.tail:
                    self.tail._next = None
                else:
                    self.head = None
            else:
                prev = node._prev
                next = node._next
                prev.next = next
                next.prev = prev
            del node

    def __repr__(self):
        str_repr = []
        current = self.head
        while current:
            str_repr.append(current.__repr__())
            current = current._next
        return " ".join(str_repr)
        
    def __contains__(self, value):
        return value in self.hashmap

