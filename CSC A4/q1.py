class Node:

    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        if self.head == None:
            self.head = self.tail = Node(data, None)
        else:
            new_tail = Node(data, None)
            self.tail.pointer = new_tail
            self.tail = new_tail

    def recursive_count(self, node):
        if node.pointer == None:
            return 1
        elif node == None:
            return 0
        else:
            return self.recursive_count(node.pointer) + 1
