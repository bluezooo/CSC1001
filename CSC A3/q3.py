###WHY_BUG????????????

import random

class ecosystem:
    def __init__(self, river_length = 0, fish = 0, bear = 0, step = 0, river = ''):
        self.river = river
        self.bear = bear
        self.fish = fish
        self.step = step
        self.river_length = river_length

    def set_river(self):
        self.river_length = int(input('Please input the length of the river > '))
        self.fish = int(input('Please input the number of the fish > '))
        self.bear = int(input('Please input the number of the bears > '))
        self.step = int(input('Please input a valid step > '))
            
        if self.fish + self.bear > self.river_length:
            print('This is not a valid ecosystem.')
            exit()
        self.river += 'F' * self.fish + 'B' * self.bear + 'N' * (self.river_length - self.fish - self.bear)
        self.river = random.sample(self.river, self.river_length)
        c = ''
        for i in self.river:
            c += i
        print('initial river:', c)
        
    def simulation(self):
        river_list = list(self.river)
        step = 0
        while step < self.step:
            step += 1
            for i in range(len(river_list)):   
                x = random.random()
                if 0 <= x <= 0.33333:
                    fx =  -1
                elif 0.33333 <= x <= 0.66666:
                    fx = 0
                else:
                    fx = 1
         
                if self.river[i] != 'N':  
                    if i == 0:
                        temp_move = abs(fx)
                    elif i == len(self.river) - 1:
                        temp_move = -abs(fx)
                    else:
                        temp_move = fx
                    
                    if self.river[i + temp_move] == self.river[i]:
                        if temp_move != 0:    
                            while True:
                                random_position = random.randint(0, len(self.river) - 1)
                                if self.river[random_position] == 'N':
                                    self.river[random_position] = self.river[i]
                                    break
                    elif self.river[i + temp_move] > self.river[i]:
                        self.river[i + temp_move] = self.river[i]
                        self.river[i] = 'N'
                    else:
                        self.river[i] = self.river[i + temp_move]
                        self.river[i + temp_move] = 'N'
            c = ''
            for i in self.river:
                c += i
            print('this is river in the', step, 'step:', c)

Ecosystem = ecosystem()
Ecosystem.set_river()
Ecosystem.simulation()
