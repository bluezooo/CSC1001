#What are problems of the following program?
class A:
    def __init__(self):
        self.__i=i

def main():
    a=A(5)
    print(a.__i)

main()

# #Reference Answer:①Change to public
# class A:
#     def __init__(self,i):
#         self.i=i

# def main():
#     a=A(5)
#     print(a.i)

# main()

# #Reference Answer:②Use a getter
# class A:
#     def __init__(self,i):
#         self.__i=i
#     def get_i(self):
#         return self.__i

# def main():
#     a=A(5)
#     print(a.get_i())

#main()
