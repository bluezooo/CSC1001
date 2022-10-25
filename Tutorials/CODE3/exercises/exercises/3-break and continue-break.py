
#break
m_list = [624235, 368, 8127]
is_find = False

for i in range(len(m_list)-1, -1, -1):
    current_num = m_list[i]
    
    while current_num > 0:
        current_dgt = current_num % 10
        if current_dgt%2 == 1:
            print('the last odd digit is %d'%current_dgt)
            is_find = True
            break
        else:
            current_num //= 10
    if is_find:
        break
















