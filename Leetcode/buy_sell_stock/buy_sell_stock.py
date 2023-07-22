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
                self.insert(Node(v))

    def first(self) -> int:
        return self.head.value

    def last(self) -> int:
        return self.tail.value


    def insert(self, node:Node):
        self.hashmap[node.value].append(node)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
             node._prev = self.tail
             self.tail._next = node
             self.tail=node

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
    

class Solution:
    def maxProfit(self, prices):
        sorted_prices = sorted(prices)
        hll = HashedLinkedList(sorted_prices)
        bestdiff = 0
        for i in range(len(prices)-1):
            hll.remove(prices[i])
            diff = hll.last() - prices[i]
            if diff > bestdiff:
                bestdiff = diff
        return bestdiff

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,11,1,2,4]))

       