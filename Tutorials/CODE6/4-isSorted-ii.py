def isSorted(lst):
    lst_copy = lst
    lst.sort(reverse=False)
    if lst == lst_copy:
        return True
    return False

def main():
    lst=input("Enter elements in a list separated by space:\n").split()
    lst=[eval(x) for x in lst]
    if isSorted(lst):
        print("The list is already sorted.")
    else:
        print("The list is not sorted.")

main()
