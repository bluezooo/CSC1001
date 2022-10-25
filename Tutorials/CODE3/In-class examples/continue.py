print('========for loop without continue========')
for i in range(5):
    print(i)

print('========for loop with continue========')

for i in range(5):
    if i==3:
        continue
    print(i)
    
print('========double-layer for loop with continue========')

for i in range(5):
    print(i)
    for j in ['a','b','c']:
        if j=='b':
            continue
        print(j)
