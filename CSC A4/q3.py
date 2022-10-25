hanoi = list()

def HanoiTower(n):
    global hanoi
    hanoi.append(('A', 'C', n))
    while len(hanoi):
        top = hanoi[len(hanoi) - 1] 
        hanoi = hanoi[0: len(hanoi) - 1]
        if top[2] != 1:
            exchange = chr(198 - ord(top[0]) - ord(top[1]))
            hanoi.append((exchange, top[1], top[2] - 1))
            hanoi.append((top[0], top[1], 1))
            hanoi.append((top[0], exchange, top[2] - 1))
        else:
            print(top[0], '-->', top[1])
            
try:
    n = int(input('The value n (number of disks):'))
except:
    print('Please input a positive integer.')
HanoiTower(n)

