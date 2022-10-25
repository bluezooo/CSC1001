class A:
    def __init__(self):
        self.a = 'a'
        
    def my_print(self):
        print('this is A')

    def __aa(self):
        print('aa')

class B(A):
    def __init__(self):
        pass

class C(A):
    def __init__(self):
        super().__init__()


print('test on B')
b = B()
try:
    print(b.a)
except:
    print('fail to call a from parent')

try:
    print(b.__aa())
except:
    print('fail to call __aa from parent')

try:
    b.my_print()
except:
    print('fail to call my_print from parent')


print('\ntest on C')
c = C()
print(dir(c))
try:
    print(c.a)
except:
    print('fail to call a from parent')

try:
    print(c.__aa())
except:
    print('fail to call __aa from parent')

try:
    c.my_print()
except:
    print('fail to call my_print from parent')
