#approximate the square root
def sqrt(n):
    lastGuess = 2
    while True:
        nextGuess = (lastGuess + n / lastGuess) / 2
        if -0.0001 <= nextGuess - lastGuess <= 0.0001:
            break
        lastGuess = nextGuess
    return lastGuess

def main():
    while True:     #get a valid input number n
        try:
            n = float(input('Please input a non-negative real number to take its square root.'))
            if n >= 0:
                break
        except:
            print('please enter the number again.')
    print(format(sqrt(n), "3.5f"))
    return

main()

