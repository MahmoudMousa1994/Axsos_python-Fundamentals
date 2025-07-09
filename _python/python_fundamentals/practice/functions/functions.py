def add(a,b):
    x=a+b
    return x
new_val = add(3,5)
print(new_val)

# parameters and arguments
def say_hi(name):
    print("Hi, "+name)
say_hi('Mahmoud')
say_hi('Saja')

# returning values
def say_hi(name):
    return "Hi "+ name
greeting = say_hi("Mahmoud")
print(greeting)