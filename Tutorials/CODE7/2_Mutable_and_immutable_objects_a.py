class Count:
    def __init__(self,count=0):
        self.count=count

def increment(c1,times1):
    #I add the 'address print' before modifying the passing-in objects in the invoked function
    #please compare the addresses before and after modifying c1.count and times1
    #c1 will remain the same address, but times1's address will be changed.
    print('the address of c is     ',id(c1),'   before changing count in increment')
    print('the address of times is ',id(times1),' before changing times increment')
    print()
    c1.count+=1
    times1+=1
    print('the address of c is     ',id(c1),'   after changing count in increment')
    print('the address of times is ',id(times1),' after changing times increment')
    print()

def main():
    c=Count()
    times=0
    print('the address of c is     ',id(c),'   before calling increment')
    print('the address of times is ', id(times),' before calling increment')
    print("count is",c.count)
    print("times is",times)
    print()

    
    print('call increment()')
    increment(c,times)
    print('the address of c is     ',id(c),'   after calling increment')
    print('the address of times is ', id(times),' after calling increment')
    print("count is",c.count)
    print("times is",times)
    print()
    
main()
