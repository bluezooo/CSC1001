from myQueue import ListQueue
from Customer import Customer
from Server import Server
from math import exp
from random import random

#timUnit=0.1second
timeUnit=0.1

#How many units are there in 1min
NumUnit=int(60/timeUnit)

def arrivalTime(lamda):
    epsilon=0.01

    sumProb=0
    c=-1
    while 1-sumProb>epsilon:
        c+=1
        Pc=lamda/NumUnit*exp(-lamda/NumUnit*c)
        sumProb+=Pc
        if sumProb>1:
            sumProb-=Pc
            break
        
    #c+1 will be the maximum of arrivalTime
    ProbList=[0]*(c+1)
    #The probability for arriving at c=1s
    ProbList[0]=lamda/NumUnit+lamda/NumUnit*exp(-lamda/NumUnit)
    for i in range(2,c+1):
        ProbList[i-1]=lamda/NumUnit*exp(-lamda/NumUnit*i)
    ProbList[c]=1-sumProb
    sumPrevious=0
    randNum=random()
    for i in range(1,c+2):
        sumAfter=sumPrevious+ProbList[i-1]
        if randNum>sumPrevious and randNum<=sumAfter:
            return i
        else:
            sumPrevious=sumAfter
    
class Simulation:
    def __init__(self,lamda,mu,totalTime):
        #Parameters supplied by the user
        self.__lamda=lamda
        self.__mu=mu
        self.__totalTime=totalTime
        #Simulation components
        self.__CustomerQ=ListQueue()
        #Computed during the simulation
        self.__totalWaitTime=0
        self.__numCustomers=0
        
    #Run the simulation using the parameters supplied earlier
    def run(self):
        self.server=Server()
        self.idNum=1
        for curTime in range(self.__totalTime+1):
            self.__handleArrival(curTime)
            self.__handleBeginService(curTime)
            self.__handleEndService(curTime)
##            print('current time',curTime)
##            print(self.__CustomerQ)

    #get the average waiting time of each customer
    def getaverageWaitTime(self):
        numServed=self.__numCustomers-len(self.__CustomerQ)
        return float(self.__totalWaitTime/NumUnit)/numServed

    #get the length of customer in queue
    def getlenQueue(self):
        return len(self.__CustomerQ)
        
    #Print the simulation results
    def printResults(self):
        numServed=self.__numCustomers-len(self.__CustomerQ)
        avgWait=float(self.__totalWaitTime/NumUnit)/numServed
        print("Total number of customers=",self.__numCustomers)
        print("Number of customers served=",numServed)
        print("Number of customers remaining in line=%d"%len(
            self.__CustomerQ))
        print("The average wait time was %4.2f mins."%avgWait)
    
    def __handleArrival(self,curTime):
        if curTime==0:
            self.arTime=arrivalTime(self.__lamda)
            #To store the time when previous customer arrives
            self.customerarTime=0
##            print('arTime:',self.arTime,'current time:',curTime)
        else:
            if curTime==self.customerarTime+self.arTime:
                c=Customer(self.idNum,curTime)
                self.__CustomerQ.enqueue(c)
                self.__numCustomers+=1
                self.idNum+=1
                self.customerarTime=curTime
                self.arTime=arrivalTime(self.__lamda)
##                print('arTime:',self.arTime,'current time:',curTime)
        
    def __handleBeginService(self,curTime):
        if not self.__CustomerQ.is_empty() and self.server.getservedCustomer()==None:
            customer=self.__CustomerQ.first()
            #Begin to serve the first arrival customer when he arrives
            if customer.getidNum()==1:
                if curTime==customer.getarrivalTime():
                    self.serTime=arrivalTime(self.__mu)
##                    print('serTime:',self.serTime,'current time:',curTime)
                    self.server.startService(customer,curTime+self.serTime)
            else:
                self.server.startService(customer,curTime+self.serTime)
            
    def __handleEndService(self,curTime):
        if curTime==self.server.getstopTime():
            customer=self.server.stopService()
            self.serTime=arrivalTime(self.__mu)
##            print('serTime:',self.serTime,'current time:',curTime)
            #Waiting time is the time after served-the time he comes??
            self.__totalWaitTime+=curTime-customer.getarrivalTime()
            self.__CustomerQ.dequeue()

def main():
    simulation=Simulation(9,10,480*NumUnit)
    simulation.run()
    simulation.printResults()

main()

##def main():
##    averageLenQueue=0
##    averageWaitTime=0
##    numSimulation=10000
##    for i in range(numSimulation):
##        simulation=Simulation(9,10,480*NumUnit)
##        simulation.run()
##        averageLenQueue+=simulation.getlenQueue()
##        averageWaitTime+=simulation.getaverageWaitTime()
##    averageLenQueue/=numSimulation
##    averageWaitTime/=numSimulation
##    print('Average Length of Queue:',averageLenQueue)
##    print('Average Waiting Time for each customer:',averageWaitTime)
##    
##
##main()

