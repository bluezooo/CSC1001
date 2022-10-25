##Define a function to obtain the reverse of a number
def reverse(_number):
    reversenumber = ''
    while _number != 0:
        reversenumber += str(_number%10)
        _number//=10
    reversenumber = int(reversenumber)
    return reversenumber
    
##Define a function to judge whether a number is a palindrome
def is_not_Palindrome(_number):
    if _number == reverse(_number):
        return False
    else:
        return True

##Define a function to judge whether a number is a prime
def isPrime(_number):
    divisor=2
    while divisor <= _number/2:
        if _number % divisor==0:
            return False
        else:
            divisor += 1
            continue
    return True 

##Define a function to judge whether a prime is a emirp
def is_emirp(_number):
    reversed = 0 
    reversed = int(str(_number)[::-1])

    if isPrime(reversed) and isPrime(_number) and is_not_Palindrome(_number):
        return True
    else:
        return False

##Define a main function to display 100 numbers which is palindrome and prime
def main():
    count=0
    number=2                     #Begin from the smallest palindrome and prime 2
    while count<100:
        if is_emirp(number):
            print("%6d"%number, end='')
            count+=1
            number+=1
        else:
            number+=1
            continue             #Turn to the next number if it is not what we want
        if count%10==0:          #Change line after every 10 numbers
            print()

main()