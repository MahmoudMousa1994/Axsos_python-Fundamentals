class Calculator:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def add(self, a, b):
        sum = a + b
        print(f"{a} + {b} = {sum}")
        return self
    
    def subtract(self, a, b):
        sub = a - b
        print(f"{a} - {b} = {sub}")
        return self

    def multiply(self, a, b):
        multi = a * b
        print(f"{a} X {b} = {multi}")
        return self
    
    def divide(self, a, b):
        if type(a)!= int or type(b)!= int:
            print("invalid input")
            return self

        elif b == 0:
            print("cant divide by zero")
            return self

        else:
            divison = a/b
            print(f"{a} / {b} = {divison}")
            return self


math = Calculator()

math.add(10,5).subtract(65,98).multiply(6,5).divide(5,True).divide(5,"9").divide(5,0).divide(5,5)