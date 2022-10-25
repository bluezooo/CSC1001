class Customer:
    def __init__(self,idNum=0,arrivalTime=0):
        self.__idNum=idNum
        self.__arrivalTime=arrivalTime
    def setidNum(self,idNum):
        self.__idNum=idNum
    def setarrivalTime(self,arrivalTime):
        self.__arrivalTime=arrivalTime
    def getidNum(self):
        return self.__idNum
    def getarrivalTime(self):
        return self.__arrivalTime
    def __str__(self):
        return 'Customer '+str(self.__idNum)

##c=Customer()
##c.setidNum(1)
##c.setarrivalTime(0.1)
##print(c.getidNum(),c.getarrivalTime())
##print(c)
        
