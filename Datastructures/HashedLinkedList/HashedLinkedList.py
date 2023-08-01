from collections import defaultdict
class Node:
    def __init__(self, value):
        self.value = value
        self._prev:Node = None
        self._next:Node = None
    
    def __repr__(self) -> str:
         return f"{self.value}"


class LinkedListIterator:
    def __init__(self, head):
        self.current: Node = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.value
            self.current = self.current._next
            return data

class HashedLinkedList:
    def __init__(self, __iterable: None = None):
        self.head: Node = None
        self.tail: Node = None
        self.hashmap = defaultdict(list)
        self.length = 0
        if __iterable: 
            for v in __iterable:
                node = Node(v)
                self.append(node)
    
    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def __len__(self):
        return self.length

    def insert(self, node:Node):
        self.length+=1
        self.hashmap[node.value].append(node)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
             newNode = node
             newNode._next = self.head
             self.head._prev = newNode
             self.head=newNode

    def append(self, node:Node):
        self.length += 1
        self.hashmap[node.value].append(node)
        if not self.tail:
            self.tail = node
            self.head = self.tail
        else:
             newNode = node
             newNode._prev = self.tail
             self.tail._next = newNode
             self.tail=newNode

    def remove(self, value):
        self.length -= 1
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
                prev._next = next
                next._prev = prev
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

        

if __name__ == "__main__":
    hll = HashedLinkedList([1,2,3,4,5])
    for n in LinkedListIterator(hll.head):
        print(n)
    hll.remove(5)
    hll.remove(4)
    hll.remove(3)
    hll.remove(2)
    hll.remove(1)
    print(len(hll))