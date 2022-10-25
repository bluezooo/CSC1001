try:
    final= float(input("Enter the final account value:"))
    InterestRate = float(input("Enter the annual interest rate in percentage(%):"))
    Years = float(input("Enter the number of years:"))
    
    initial = final / (1+InterestRate / 100)**Years
    print('The initial value is:', initial)

except:
    print("invalid input")

#in case that the python IDLE directly exit without output
input('Enter any command to exit') 