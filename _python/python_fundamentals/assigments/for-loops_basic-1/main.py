# 1. Baisc
for i in range(151):
    print(i)

# 2. multiples of Five
for i in range(5,1001,5):
    print(i)

# 2. multiples of Five another method
for i in range(1001):
    if i % 5 == 0:
        print(i)

# 3.counting, the Dojo way
for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif  i % 5 == 0:
        print("Coding")
    else:
        print(i)


# 4. whoa. that sucker's huge
sumodd = 0
for i in range(500001):
    if i % 2 == 1:
        sumodd +=i
print(sumodd)

# 5.Countdown by fours 
x =[]
for i in range(2018,0,-4):
    x.append(i)
print(x)

# 6.flexible counter
lowNum=2
highNum=9
mult=3
for i in range(highNum,lowNum,-1):
    if i % mult == 0:
        print(i)