def insertion(l):
    for i in range(1,len(l)):
        j = i-1
        x = l[i]
        while j>=0 and l[j]>x:
            l[j+1]=l[j]
            j = j-1
        l[j+1]=x
    return l
L=[1,5,4,0]
print(insertion(L))