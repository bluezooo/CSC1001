import types
class Account:
    def __init__(self,ID=0,balance=100,annualInterestRate=0):
        self.setId(ID)
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    
    def setId(self,ID=0):
        self.__ID=ID
    
    def setBalance(self,balance=0):
        self.__balance=balance
    
    def setAnnualInterestRate(self,annualInterestRate=0):
        self.__annualInterestRate=annualInterestRate
    
    def getId(self):
        return self.__ID
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def getMonthlyInterestRate(self):
        MonthlyInterestRate=self.__annualInterestRate/12
        return MonthlyInterestRate
    
    def getMonthlyInterest(self):
        MonthlyInterest=self.__balance*self.getMonthlyInterestRate()/100
        return MonthlyInterest
    
    def withdraw(self,ammount=0):
        self.__balance=self.__balance-ammount
    
    def deposit(self,ammount=0):
        self.__balance=self.__balance+ammount

def run(self):
    print("...%s正在跑。。"%self.new_ID)

def main():
    Alice=Account(1122,20000,4.5)
    Alice.new_ID = 123
    print(Alice.getId())
    print(Alice.new_ID)

 

    Alice.run = types.MethodType(run,Alice)#将run这个函数添加为方法
    Alice.run()


    # print('-'*66)
    # print('%-8s%-12s%-26s%-18s'%('ID:','Balance:','Monthly interest rate(%):','Monthly interest:'))
    # print(('%-8d%-12.2f%-26.2f%-18.2f')%(Alice.getId(),Alice.getBalance(),Alice.getMonthlyInterestRate(),Alice.getMonthlyInterest()))
    # print('-'*66)
    # Alice.withdraw(2500)
    # print('-'*66)
    # print("After withdraw $2500:")
    # print('%-8s%-12s%-26s%-18s'%('ID:','Balance:','Monthly interest rate(%):','Monthly interest:'))
    # print(('%-8d%-12.2f%-26.2f%-18.2f')%(Alice.getId(),Alice.getBalance(),Alice.getMonthlyInterestRate(),Alice.getMonthlyInterest()))
    # print('-'*66)
    # Alice.deposit(3000)
    # print('-'*66)
    # print("After deposit $3000:")
    # print('%-8s%-12s%-26s%-18s'%('ID:','Balance:','Monthly interest rate(%):','Monthly interest:'))
    # print(('%-8d%-12.2f%-26.2f%-18.2f')%(Alice.getId(),Alice.getBalance(),Alice.getMonthlyInterestRate(),Alice.getMonthlyInterest()))
    # print('-'*66)

main()