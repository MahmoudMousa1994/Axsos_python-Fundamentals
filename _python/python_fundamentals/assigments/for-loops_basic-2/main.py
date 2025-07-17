# 1. bigge size
def biggie_size(x):
    big_list =[]
    for i in range(len(x)):
        if x[i]>0:
            big_list.append("big")
        else:
            big_list.append(x[i])
    print(big_list)
biggie_size([-1,-4,5,-7,-5,6,8])

# 2.count positive 
def count_positive(x):
    cp=[]
    for i in range(len(x)):
        if x[i]>0:
            cp.append(x[i])
    x[len(x)-1] = len(cp)
    return x
print(count_positive([-1,-7,-6,4,8,-1,0,9,0]))

# 3. sum total
def sum_total(x):
    st=0
    for i in range(len(x)):
        st+=x[i]
    return st
print(sum_total([1,2,3,4]))

# 4. average
def average(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i]
    return sum/len(x)
print(average([1,2,3,4]))

# 5.length
def length(x):
    listlength = 0
    for i in range(len(x)):
        listlength += 1
    return listlength
print(length([1,2,3,5,9,7,5]))
print(length([]))

# 6.minimum
def minimum(x):
    if len(x)==0:
        return False
    elif len(x) !=0:
        min = x[0]
        for i in range(len(x)):
            if x[i]<min:
                min=x[i]
        return min
print(minimum([]))
print(minimum([5,7,9,66,4,2,1,-6]))

# 7.maximum
def maximum(x):
    if len(x)==0:
        return False
    elif len(x) !=0:
        max = x[0]
        for i in range(len(x)):
            if x[i]>max:
                max=x[i]
        return max
print(maximum([]))
print(maximum([5,7,9,66,4,2,1,-6]))

# 8 ultimate analysis
def ultimate_analysis(x):
    ua={}
    sum=0
    min = x[0]
    max = x[0]
    for i in range(len(x)):
        sum+=x[i]
        if x[i]<min:
            min=x[i]
        elif x[i]>max:
            max=x[i]
    ua["sumTotal"]=sum
    ua["average"]=sum/len(x)
    ua["minimum"]= min
    ua["maximum"]=max
    ua["length"]=len(x)

    return ua
print(ultimate_analysis([37,2,1,-9]))

# 9.reverse list
def reverse_list(x):
    left = 0
    right = len(x)-1
    while left<right:
        x[left],x[right]=x[right],x[left]
        left += 1
        right -=1
    return x
print(reverse_list([6,4,9,2,1,7,-2,6,]))
# note : TA Ibraheim Khalil told me about the two pointer technique in a previous js assigment review

# 9.reverse list another method
def reverse_list(x):
    for i in range(len(x)//2):
        x[i],x[-1-i]=x[-1-i],x[i]
    return x

print(reverse_list([6,4,9,2,1,7,-2,6,]))


