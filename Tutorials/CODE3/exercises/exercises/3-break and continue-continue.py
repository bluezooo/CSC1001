
#continue
sum_dgt = 0

for i in range(len(m_list)):
    current_num = m_list[i]
    
    while current_num > 0:
        current_dgt = current_num%10
        current_num //= 10
        
        if current_dgt%2 != 1:
            continue
        
        sum_dgt += current_dgt
            
print('the sum of all odd digits in the list is %d'%sum_dgt)















