class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

m_list = [1,2,3]

obj_a = A(m_list)
obj_b = B(m_list)

m_list.reverse()
obj_a.a[0] = 5

print(obj_b.b)
