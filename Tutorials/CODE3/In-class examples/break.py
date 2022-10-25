print('========for loop without break========')
for i in range(5):
    print(i)

print('========for loop with break========')

for i in range(5):
    if i==3:
        break
    print(i)
    
print('========double-layer for loop with break========')

for i in range(5):
    print(i)
    for j in ['a','b','c']:
        if j=='b':
            break
        print(j)
