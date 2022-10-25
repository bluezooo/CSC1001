class Node:
    def __init__(self,e,node):
        self.element=e
        self.pointer=node

class LinkedQueue:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            #①
            return self.head.element

    def end(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            #②end=self.tail.element
            node=self.head
            while node != None:
                end=node.element
                node=node.pointer
            return end

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            #③
            answer=self.head.element
            self.head=self.head.pointer
            self.size-=1
            if self.is_empty():
                self.tail=None
            return answer

    def enqueue(self,e):
        #④
        newest=Node(e,None)
        if self.is_empty():
            self.head=newest
        else:
            self.tail.pointer=newest
        self.tail=newest
        self.size+=1

    def __str__(self):
        #⑤
        queue=[]
        node=self.head
        while node != None:
            queue.append(str(node.element))
            node=node.pointer
        return str(queue)

q=LinkedQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q)
print(q.first())
print(q.end())



##class Node:
##    def __init__(self,e,node):
##        self.element=e
##        self.pointer=node
##
##class LinkedQueue:
##    
##    def __init__(self):
##        self.head=None
##        self.tail=None
##        self.size=0
##
##    def __len__(self):
##        return self.size
##
##    def is_empty(self):
##        return self.size==0
##
##    def first(self):
##        if self.is_empty():
##            print('Queue is empty.')
##        else:
##            #①
##
##    def end(self):
##        if self.is_empty():
##            print('Queue is empty.')
##        else:
##            #②
##
##    def dequeue(self):
##        if self.is_empty():
##            print('Queue is empty.')
##        else:
##            #③
##
##    def enqueue(self,e):
##        #④
##
##    def __str__(self):
##        #⑤
##
##q=LinkedQueue()
##q.enqueue(1)
##q.enqueue(2)
##q.enqueue(3)
##q.enqueue(4)
##print(q.dequeue())
##print(q)
##print(q.first())
##print(q.end())



        
