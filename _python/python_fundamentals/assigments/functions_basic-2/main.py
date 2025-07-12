# 1.count down 
down = []
def countdown(x):
    for i in range(5,-1,-1):
        down.append(i)
countdown(5)
print(down)

# 1.count down another method
def countdown(x):
    down = []
    for i in range(5,-1,-1):
        down.append(i)
    return down
print(countdown(5))

# 2.print and return
def printAndReturn(x,y):
    print(x)
    return y
print(printAndReturn(9,4))

# 3.first plus length
def first_plus_length(x):
    return(x[0]+len(x))
print(first_plus_length([9,8,7,6,5,4]))

# values greater than second
def values_greater_than_second(x):
    vgts =[]
    for i in range(len(x)):
        if x[i]> x[1]:
            vgts.append(x[i])
    print(len(vgts))
    return vgts
print(values_greater_than_second([6,3,4,2,3,8,1,0,5]))

# 5.this length, that value
def length_and_value(x,y):
    lav = []
    for i in range(x):
        lav.append(y)
    return lav
print(length_and_value(4,7))
print(length_and_value(9,4))

