class Node:
    def __init__(self, value):
        self.value=value
        self._prev=None
        self._next=None

    def __repr__(self) -> str:
         return f"{self.value}"

class LinkedList:
    def __init__(self, __iterable: None = None):
            self.head: Node = None
            self.tail: Node = None
            if __iterable:
                 for n in __iterable:
                     self.insert(n)

    def insert(self, value):
        if (not self.head):
            self.head = Node(value)
            self.tail = self.head
        else:
             newNode = Node(value)
             newNode._next = self.head
             self.head._prev = newNode
             self.head=newNode
                 
    def append(self, value):
        if (not self.tail):
            self.tail = Node(value)
            self.head = self.tail
        else:
             newNode = Node(value)
             newNode._prev = self.tail
             self.tail._next = newNode
             self.tail=newNode
             
    # Gets node with value  
    def get(self, value) -> Node:
        current = self.head
        while current:
            if current.value == value:
                 return current
            current = current._next
        return None

    def remove(self, value):
        if not self.head:
            return False
        
        if (self.head.value == value):
            self.head = self.head._next
            if self.head:
                self.head._prev = None
            else:
                self.tail = None
            return True
        elif (self.tail.value == value):
            self.tail = self.tail._prev
            if self.tail:
                self.tail._next = None
            else:
                self.head = None
            return True
        
        current = self.head
        while current:
            if current.value == value:
                prev = current._prev
                next = current._next
                prev._next = next
                next._prev = prev
                return True
            current = current._next
        return False
    
    def __repr__(self):
        str_repr = []
        current = self.head
        while current:
            str_repr.append(current.__repr__())
            current = current._next
        return " ".join(str_repr)
    
if __name__ == "__main__":
    ll = LinkedList([1,2,3,4,5])
    print(ll.get(5))
    ll.remove(5)
    ll.remove(4)
    ll.remove(1)
    ll.remove(3)
    print(ll)