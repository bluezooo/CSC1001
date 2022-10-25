from Customer import Customer

class Server:
    def __init__(self):
        self.__customer=None
        self.__stopTime=-1
    def getservedCustomer(self):
        return self.__customer
    def getstopTime(self):
        return self.__stopTime
    def startService(self,customer,stopTime):
        self.__customer=customer
        self.__stopTime=stopTime
    def stopService(self):
        theCustomer=self.__customer
        self.__customer=None
        return theCustomer
    def __str__(self):
        return str(self.__customer)+' is being served.'

##s=Server()
##c=Customer(1,0.1)
##s.startService(c,0.2)
##print(s)
##print(s.stopService())
##print(s)

