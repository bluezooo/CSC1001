from math import exp
from random import random

#timUnit=0.1second
timeUnit=0.1

#How many units are there in 1min
NumUnit=int(60/timeUnit)    # one minute contines how many timeunit

def arrivalTime(lamda):
    #epsilon control the precision to decide after when we ignore the possiblity for arrival
    epsilon=0.01
    sumProb=0
    #c is the possible arrival time
    c=-1
    while 1-sumProb>epsilon:
        c+=1
        Pc=lamda/NumUnit*exp(-lamda/NumUnit*c)  #compute the probability of c_th time unit
        sumProb+=Pc
        #We don't allow total possiblity to exceed 1
        if sumProb>1:
            sumProb-=Pc
            break
        
    #c+1 will be the maximum of arrivalTime
    ProbList=[0]*(c+1)
    #The probability for arriving at c=1 time unit
    ProbList[0]=lamda/NumUnit+lamda/NumUnit*exp(-lamda/NumUnit)
    for i in range(2,c+1):
        ProbList[i-1]=lamda/NumUnit*exp(-lamda/NumUnit*i)
    ProbList[c]=1-sumProb
##    print(ProbList)
##    print(c+1)
    sumPrevious=0
    randNum=random()
    for i in range(1,c+2):
        sumAfter=sumPrevious+ProbList[i-1]
        if randNum>sumPrevious and randNum<=sumAfter:
            return i
        else:
            sumPrevious=sumAfter

def test():
    #Result.txt will count the how many times each c occurs, smaller c should have large possibility for arrival
    file=open('arrivalTime.txt','w')           
    for i in range(1000):
        file.write(str(arrivalTime(5))+'\n')
    file.close()
    file=open('arrivalTime.txt','r')
    countDict={}
    for line in file.readlines():
        arTime=int(line.strip())
        countDict[arTime]=countDict.get(arTime,0)+1
    file.close()
    file=open('Result.txt','w')
    countList=list(countDict.keys())
    countList.sort()
    for arTime in countList:
        file.write(str(arTime)+'\t'+str(countDict[arTime])+'\n')
    file.close()

test()
