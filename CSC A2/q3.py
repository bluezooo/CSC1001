##Return this number if it is a single digit
##The sum of the two digits
def sumOfDoubleEvenPlace(number):
    number_list = list(map(int, str(number)))
    even_list = list()
    
    for i in number_list[-2::-2]: 
        if i * 2 >= 10:
            digit = i * 2 % 10 + 1
        else:
            digit = i * 2
        even_list.append(digit)
    
    return sum(even_list)

##Return sum of odd place digits in number
def sumOfOddPlace(number):
    number_list = list(map(int, str(number)))
    odd_list = list()
    
    for i in number_list[-1::-2]: 
        odd_list.append(i)
    
    return sum(odd_list)

##Return True if the card number is valid
def isValid(number):
    if (sumOfDoubleEvenPlace(number)\
        + sumOfOddPlace(number)) % 10 == 0:
        return True
    else:
        return False

def main():
    while True:
        try:
            number = int(input('Please enter a card number to check if it is valid : '))
            if number > 0:
                break
            else:
                print('Please enter a positive integer')
        except:
            print('Please enter a positive integer')

    if isValid(number):
        print('The credit card number is valid')
    else:
        print('The credit card number is invalid.')

main()