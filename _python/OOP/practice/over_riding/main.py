# overriding
class Parent:
    def method_a(self):
        print("invoke PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoke CHILD method_a!")

dad = Parent()
son = Child()
dad.method_a()
son.method_a()

# Polymorphism
class Person:
    def pay_bill(self):
        raise NotImplementedError

class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! keeo the change!")

class Gradstudent(Person):
    def pay_bill(self):
        print("Can I owe you ten buckes or do the dishes?")

a = Person()
# a.pay_bill()
b = Millionaire()
b.pay_bill()
c =Gradstudent()
c.pay_bill()

