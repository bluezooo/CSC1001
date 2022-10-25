##①
class A:
    def __new__(self):
        print(type(self))
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")

    def run(self):
        #print(type(self))
        print('run')

class B(A):
    def __new__(self):
        print("B's __new__() invoked")

    def __init__(self, b):
        print("B's __init__() invoked")

def main():
    b=B()
    #b.run()
    a=A()
    a.run()

main()

##②
# class A:
#     def __new__(self):
#         print(type(self))
#         self.__init__(self)
#         # self.__init__()
#         print("A's __new__() invoked")

#     def __init__(self):
#     # def __init__():
#         print("A's __init__() invoked")

# class B(A):
#     def __new__(self):
#         # self.__init__()
#         self.__init__(self)
#         print("B's __new__() invoked")

#     # def __init__():
#     def __init__(self):
#         print("B's __init__() invoked")

# def main():
#     b=B()
#     a=A()

# main()

##
##③
# class A:
#     def __new__(self):
#         self.__init__(self)
#         print("A's __new__() invoked")

#     def __init__(self):
#         print("A's __init__() invoked")

# class B(A):
#     def __init__(self):
#         print("B's __init__() invoked")

# def main():
#     b=B()
#     a=A()

# main()


