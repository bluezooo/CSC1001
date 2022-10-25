import copy

lst = [1, 2, [3, 4, 5]]

lst_c = copy.copy(lst)
lst_dc = copy.deepcopy(lst)

print('original lst: ' + str(lst))
print()

lst[0] = 'a'
print('========Modify inner int========')
print('lst: ' + str(lst))
print('lst_copy: ' + str(lst_c))
print('lst_deep_copy: ' + str(lst_dc))
print()

lst[2][2] = 6
print('========Modify inner list========')
print('lst: ' + str(lst))
print('lst_copy: ' + str(lst_c))
print('lst_deep_copy: ' + str(lst_dc))
