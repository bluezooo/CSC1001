##Prompt up the indicator for user to enter
number=eval(input("Enter a number between 0 and 999:"))

#number = 123
##Use the variable to do the operation
sumup=0
sumup += number%10
number//=10
sumup += number%10
number//=10
sumup += number%10

##Display the result
print("Sum up all the digits as:",sumup)
