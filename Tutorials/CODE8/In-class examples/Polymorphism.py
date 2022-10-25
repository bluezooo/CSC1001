class Animal:
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print('say miaomiao')

class Dog(Animal):
    def talk(self):
        print('say wangwang')

class Pig(Animal):
    def talk(self):
        print('say aoao')

#......add more implementations, extensibility

c = Cat()
d = Dog()
p = Pig()

def func(obj):
    obj.talk()

#one way to call
func(c)
func(d)
func(p)
