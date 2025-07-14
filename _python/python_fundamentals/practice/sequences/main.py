my_list = [99,4,2,5,-3]
my_tuble = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
print(my_tuble[1:])
print(my_str[:3])
print(my_tuble[2:4])
print(my_list,my_tuble,my_str)

print(max(my_str))
print(sum(my_list))
print(list(map(lambda x: x **2, my_tuble)))
print(min(my_str))
print(sorted(my_list))