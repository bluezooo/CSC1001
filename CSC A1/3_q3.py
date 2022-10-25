
try:
    m = float(input('Please input a number'))
except:
    print('invalid input')
else:
    if m>=0: 
        n=0
        while n**2<=m :
            n += 1
        print(n)
    else:
        print('negative infinity')

#in case that the python IDLE directly exit without output
input('Enter any command to exit') 