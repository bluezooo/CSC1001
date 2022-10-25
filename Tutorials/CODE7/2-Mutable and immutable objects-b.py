class Count:
    def __init__(self,count=0):
        self.count=count

def m(c1):
    print('the address of c1 is ',id(c1),' before creating new object in m')

    #create a new object and also local,
    #you don't change anything to the passed into object
    c1 = Count(5)
    print('the address of c1 is ',id(c1),' after creating new object in m')

    # overide the obj c,
    #if you have a variable to receive this return object
    return c1

def main():
    c=Count()
    print('count is', c.count)
    print('the address of c is  ',id(c),' before calling m')

    m(c)      #pass object c into m(), do not take return value
    print('count is', c.count)
    print('the address of c is  ',id(c),' without return value')

    c = m(c)  #pass object c into m() again, take return value
    print('count is', c.count)
    print('the address of c is  ',id(c),' with return value')

main()
