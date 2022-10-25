##Prompt the user to enter the monthly saving amount
monthlyDeposit=eval(input("Enter the monthly saving amount:$"))

##Calculate the account value of each month
currentValue=monthlyDeposit
##After the first month
currentValue=currentValue*(1+0.00417)
##After the second month
currentValue=(currentValue+monthlyDeposit)*(1+0.00417)
##After the third month
currentValue=(currentValue+monthlyDeposit)*(1+0.00417)
##After the fourth month
currentValue=(currentValue+monthlyDeposit)*(1+0.00417)
##After the fifth month
currentValue=(currentValue+monthlyDeposit)*(1+0.00417)
##After the sixth month
currentValue=(currentValue+monthlyDeposit)*(1+0.00417)    

##Display the result
print("After the sixth month, the account value is:$%.2f"%currentValue)
