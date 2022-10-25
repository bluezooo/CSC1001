from math import sin
from math import cos
from math import tan

def isValidfunc():           #get a valid function
    global func
    func = input("Enter the func name: ")
    if func == 'sin' or func == 'cos' or \
       func == 'tan':
        return func
    else:
        print('Please enter a valid trigonometric function')
        return False

def input_a():                #get valid input:a
    global a
    while True:
        try:
            a = float(input('Enter left end point a: '))
            break
        except:
            print('Please enter a number')

def input_b():                #get valid input:b
    global b
    while True:
        try:
            b = float(input('Enter right end point b: '))
            break
        except:
            print('Please input a number:')

def input_n():                #get valid input:n
    global n
    while True:
        try:
            n = int(input('Input number n: '))
        except:
            print('Please input a positive integer')
            continue
        if n > 0:
            break
        else:
            print('Please input a positive integer')

while True:
    if isValidfunc():
        break
    else:
        continue

while True:                 #Ensure that a is smaller than b
    input_a()
    input_b()
    if a >= b:
        print('Number a should be smaller than b')
    else:
        break

input_n()                    #main calculate part
sum = 0
func = '(b - a) / n * ' + func + \
           '(a + (b - a) / n * (i + 1 / 2))'
for i in range(n):
    sum += eval(func)
print('The sum is:', sum)

#in case that the python IDLE directly exit without output
input('Enter any command to exit') 