numberLine=input("Enter ten numbers(separated by space):\n")
numberList=numberLine.split()

##version 1
# distinctnumber=[]
# for number in numberList:
#     if number not in distinctnumber:
#         distinctnumber.append(number)

##version 2
distinctnumber = set(numberList)

#print distinct numbers
print("The distinct numbers are:",end='')
for number in distinctnumber:
    print(number,end=' ')

