class Node:
    
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer

class SinglyLinkedList:

    def __init__(self):
        t = Node(None, None)
        self.head = t
        self.tail = t

    def insert(self, data):
        if self.head.element == None:
            self.head = self.tail = Node(data, None)
        else:
            new_tail = Node(data, None)
            self.tail.pointer = new_tail
            self.tail = new_tail
        
    def quick_sort(self, node):
        self.DepthFirstSearch(node, self.tail)
        return self.head.element

    def DepthFirstSearch(self, head, tail):

        if head == tail:
            return
        pivot = head
        begin = head
        next = head.pointer
        while next != tail.pointer:
            if next.element < head.element:
                middle = head
                begin = begin.pointer
                next.element, begin.element = begin.element, next.element
            next = next.pointer
        pivot.element, begin.element = begin.element, pivot.element
        if begin != head:
            self.DepthFirstSearch(head, middle)
        if begin != tail:
            self.DepthFirstSearch(begin.pointer, tail)


