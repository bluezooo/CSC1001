class A:
    def __init__(self,newS='Welcome'):
        self.__s=newS

    def myprint(self):
        print(self.__s)

def main():
    a=A()
    a.myprint()

main()


    
