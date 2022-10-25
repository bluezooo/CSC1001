##Input the number of lines of the pyramid
numOfLine=eval(input("Enter the number of lines:"))

##Diplay each row of the pyramid
for row in range(1,numOfLine+1):
##  Display the left part of the row
    for column in range(numOfLine,1,-1):
        if column<=row:
##          Print the number
            print("%4d"%column,end='')      
        else:
##          Print space
            print("%4s"%" ",end='')          



    #Display the right part of the row
    for column in range(1,numOfLine+1):
        if column<=row:
##          Print the number
            print("%4d"%column,end='')      
        else:
##          Print space
            print("%4s"%" ",end='')
##  Change a new line to print
    print()
