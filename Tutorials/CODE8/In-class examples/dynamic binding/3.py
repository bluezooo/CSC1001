from types import MethodType
 
class Student(object):
    pass
 
def set_age(self, age):
    self.age = age
 
stu1 = Student()
stu2 = Student()
 
stu1.set_age = MethodType(set_age, stu1)
stu2.set_age = MethodType(set_age, stu2)
stu1.set_age(22)
stu2.set_age(44)
print(stu1.age)   # 22
print(stu2.age)   # 44
