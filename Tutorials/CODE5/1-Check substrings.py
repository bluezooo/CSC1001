##Define a function to check whether 'substring' is a substring of 'string'
def find(substring,string):
    index=0
    ##Start from index 0 of the string
    for i in string:
        ##Cut a string with length of 'substring' from 'string' to check whether they are the same
        if string[index:index+len(substring)]==substring:
            return index
        else:
            index+=1
            continue
    ##return -1 if 'substring' is not a substring of 'string'
    return -1

def main():
    first=input("Please enter the first string:")
    second=input("Please enter the second string:")
    if find(first,second) != -1:
        print("'%s' is a substring of '%s' and its index is %d."%(first,second,find(first,second)))
    else:
        print("'%s' is not a substring of '%s'."%(first,second))

main()
