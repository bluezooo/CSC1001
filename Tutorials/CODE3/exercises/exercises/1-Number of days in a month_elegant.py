##Prompt the user to enter the month and year
month,year = eval(input("Enter the month and year:"))

name_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month==2 and ((year%4==0 and year%100 != 0) or year%400==0):
    days_of_month[1] = 29
print("%s. %d has %d days"%(name_of_months[month-1], year, days_of_month[month-1]))
