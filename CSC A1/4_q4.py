while True:          #get a valid input
    try:
        a = int(input('Please iuput a positive integer m: '))
        if a >= 1:
            break
        else:
            print('Invalid input, please input again:')
    except:
        print('Invalid input, please input again:')

print('%-8s%-8s%-8s'%('m','m+1','m*(m+1)'))  #print the table
for i in range(1,a+1):
    print('%-8d%-8d%-8d'%(i,i+1,i*(i+1)))

#in case that the python IDLE directly exit without output
input('Enter any command to exit') 

