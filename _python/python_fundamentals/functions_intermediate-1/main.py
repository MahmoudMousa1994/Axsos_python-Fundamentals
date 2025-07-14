import random
def randInt(min=0,max=0):

    if min ==0 and max ==0:
        num = random.random()*100
    elif max !=0 :
        num= random.random()*max
    elif min !=0:
        num= random.random()*(100-min)+min
    else:
        num = random.random()*(max-min)+min
    return round(num)
    
print(randInt())
print(randInt(max=5)) 
print(randInt(min=50)) 
print(randInt(min=50, max=500))