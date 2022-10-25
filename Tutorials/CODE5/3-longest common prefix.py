
def prefix(s1,s2):
    i=0
    while i<len(s1):
##      Enlarge the prefix untill it is not common
        if s2.startswith(s1[:i+1]):
            i+=1
##      Slicing the string to get prefix
        else:
            s=s1[:i]
            break
    return s

def main():
    s1=input("Enter the first string:")
    s2=input("Enter the second string:")
    print("The longest common prefix of the two strings is \"",prefix(s1,s2),"\".",sep='')

main()
