class Flower:
    def __init__(self, name = '', number = 0, price = 0.0):
        self.name = name
        self.number = number
        self.price = price

    def set_name(self):
        self.name = input('Flower name (string) > ')
    
    def set_number(self):
        self.number = 0
        while self.number <= 0:
            number = input('Number of petals (positive integer) > ')
            try:
                self.number = int(number)
            except:
                print('Invalid input, try again.')    
    
    def set_price(self):
        self.price = 0.0
        while self.price <= 0:
            price = input('Flower price (positive float) > ')
            try:
                self.price = float(price)
            except:
                print('Invalid input, try again.')  
    
    def get_number(self):
        print('Number of petals:', self.number)
    
    def get_name(self):
            print('Flower name:', self.name)
    
    def get_price(self):
        print('Flower price:', self.price)

flower = Flower()
flower.set_name()
flower.set_number()
flower.set_price()
flower.get_name()
flower.get_number()
flower.get_price()
