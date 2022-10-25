def task1(t):
    return t+1
def task2(t):
    return t+2
def main(t2):
    print(task2(task1(t2))+3)
    return 
main(0)