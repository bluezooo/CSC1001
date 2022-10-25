while True:
    try:
        number = input('Enter a positive integer:')
        integer = int(number)
        # if integer<=0:
        #     print('invalid input')
        # else:
        numberList = list(number)
        for i in range(len(numberList)):
            print(numberList[i])
        break
    except:
        print('Invalid input, please input again:')

#in case that the python IDLE directly exit without output
input('Enter any command to exit') 