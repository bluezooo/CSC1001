from types import MethodType
 
class Student (object):
    pass
 
def set_age(self, age):
    print(self)
    self.age = age
 
Student.set_age = MethodType(set_age, Student)
stu1 = Student()
stu2 = Student()
 
stu1.set_age(23)
stu2.set_age(99)
print(stu1.age)   # 99
print(stu2.age)   # 99
print(id(stu1.set_age), id(stu2.set_age))
print(id(stu1.__init__), id(stu2.__init__))
print(id(stu1.age), id(stu2.age))
