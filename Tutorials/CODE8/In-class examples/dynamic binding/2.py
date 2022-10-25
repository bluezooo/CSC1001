from types import MethodType
 
class Student(object):
    def __init___(self, name, age):
        self.name = name
        self.age = age
 
def run(self):
    print("this is run method ", self)
 
stu = Student()
stu.run = MethodType(run, stu)
stu.run()
