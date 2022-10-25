integerLine = input("Enter several integers in the interval [1,100](separated by space):\n")
integerList = integerLine.split()

countDict=dict()
for integer in integerList:
    countDict[integer] = countDict.get(integer,0) + 1

time = ['time', 'times']
for key,value in countDict.items():
    print("%s occurs %d %s."%(key, value, time[value>1]))