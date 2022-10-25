##②
##Prompt up the indicator for user to enter
number=eval(input("Enter a number:"))
##Use sumup to store the sum of digits
sumup=0
##if number is bigger than 0, there are digits to be summed, so go into the loop
while number>0:
##  sum up the digit
    sumup+=number%10
##  remove the digit already being summed
    number//=10
##Display the result
print("Sum up all the digits as:",sumup)
##②




















