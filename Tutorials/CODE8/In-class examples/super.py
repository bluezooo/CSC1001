class A:
    def __init__(self):
        self.my_print()
        self.__i = 1
        
    def my_print(self):
        print('this is A')

class B(A):
    def __init__(self):
        super().my_print()
        self.my_print()
        
    def my_print(self):
        print('this is B')


print('create an object of A')
a = A()

print()

print('create an object of B')
b = B()
