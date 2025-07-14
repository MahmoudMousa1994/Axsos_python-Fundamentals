# traditinal
def square(num):
    x = num**2
    return(x)

# lambda
lambda num: num**2

# an elemwnt in a list
my_list = ['test_string', 99, lambda x : x**2]
print(my_list[2])
print(my_list[2](5))

# pass another function as a callback
def invoker(callback):
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

# stored in variable
add10 = lambda x: x + 10 
print(add10(2))
print(add10(98))

# returned by another function
def incrementor(num):
    start = num
    return lambda x: num + x

# lambdas and other functions
my_arr = [1,2,3,4,5]
def square(num):
    return num**2
print(list(map(square,my_arr)))


my_arr = [1,2,3,4,5]
print(list(map(lambda x :x ** 2 ,my_arr)))
