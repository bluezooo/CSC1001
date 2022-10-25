
def m_print(a, b, c=3):
    print(a)
    print(b)
    print(c)

m_print(1, 2, 3)
m_print(1, 2)
m_print(b=1, c=0, a=2)

#m_print(1)


def ret2(num1, num2):
    return num1, num2

m_num1, m_num2 = ret2(1, 2)
m_num3, _ = ret2(1, 2)
_, m_num4 = ret2(1, 2)


def is_positive(num):
    if num>0:
        return True
    else:
        return False
    print('can I be executed?')

print(is_positive(2))
print(is_positive(0))

