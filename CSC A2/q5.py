
def get_number(n_lockers):
    lockers = [False] * n_lockers
    for nth_student in range(1, n_lockers + 1):
        for nth_locker in range(1, n_lockers + 1):
            if nth_locker % nth_student == 0:
                lockers[nth_locker - 1] = not lockers[nth_locker - 1]
    return lockers

def select_open(a_list):
    open_list = list()
    count = 0
    for item in a_list:
        count += 1
        if item == True:
            open_list.append(count)
    return open_list

def main():
    n_lockers = 100
    lockers = get_number(n_lockers)
    open_list = select_open(lockers)
    print(open_list)
    return

main()