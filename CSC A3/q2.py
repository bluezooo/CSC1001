class derivative:
    def __init__(self, polynomial='',variable = '', derivatives = ''):
        self.polynomial = polynomial
        self.variable = variable
        self.derivatives = derivatives
    
    def getderivative(self):
        # remove space in the polynomial
        self.polynomial = self.polynomial.replace(' ', '').replace('-', '+-')
        
        # find the variable inputted
        new_polynomial = self.polynomial.replace('+', '1').replace('-', '1').replace('*', '1').replace('^', '1')
        for k in range(len(new_polynomial)):
            if not new_polynomial[k].isdigit():
                self.variable = new_polynomial[k]
                break

        # format every item in the polynomial to a*variable^b
        self.polynomial = self.polynomial.replace(self.variable, '1*' + self.variable + '^1')
        self.polynomial = self.polynomial.replace('*1', '').replace('1^', '')
        
        # split into monomial
        self.polynomial = self.polynomial.split('+')    
        mono_list = list()
        for i in self.polynomial:
            a = i.split('*' + self.variable +'^')
            mono_list.append(a)
        
        # get each derivative of each mono
        new_list = list()
        for mono in mono_list:
            if len(mono) == 2:
                coefficient = int(mono[0])*int(mono[1])
                power = int(mono[1]) - 1
                if power == 0:
                    new_list.append(str(coefficient))
                elif coefficient == 1:
                    new_list.append(self.variable + '^'+ str(power))
                else:
                    new_list.append(str(coefficient) + '*' + self.variable + '^' + str(power))
        
        # connect monomials into one new polynomial
        for l in range(len(new_list)):
            if l == 0:
                self.derivatives = new_list[0]
            if l >= 1:
                self.derivatives += '+' + new_list[l]
        self.derivatives = self.derivatives.replace('+-', '-')
        return self.derivatives

def main():
    myderivative = derivative(input('Enter an equation > '))
    print('The derivative is >', myderivative.getderivative())

main()