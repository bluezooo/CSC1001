while True:                            #get valid input
    try:
        num=int(input("please enter an integer"))
        primelist=list()
        if num >=2: 
            break
        else:
            print('No prime founded, please try it again；')
    except:
        print('Invalid input, please input it again:')

for digit in range(2,num):                #add primes to the list
    flag = True
    for i in range (2,int(digit**0.5+1)):
        if digit %i == 0:
            flag = False
            break
    if flag:
        primelist.append(digit)
            
print("ALL the prime numbers smaller than",num,"are:")
count = 0                 #print the list
for item in primelist:
    itemString = str(item)
    numFormatted = itemString.ljust(3)
    count += 1
    if count%8 == 0:
        print(numFormatted, end = '\n')
    else:
        print(numFormatted, end = ' ')

#in case that the python IDLE directly exit without output
input('Enter any command to exit') 