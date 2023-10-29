
class Node():
    def __init__(self, value, next = None, prev = None) -> None:
        self.value = value
        self.next = next 
        self.prev = prev 
    def add_next(self, value):
        if self.next is None:
            self.next = Node(value)
            self.next.prev = self
        else:
            self.next.add_next(value)


 