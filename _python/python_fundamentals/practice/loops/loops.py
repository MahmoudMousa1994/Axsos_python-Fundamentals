# for loops with range
for x in range(0, 10, 1):
    print(x)
for x in range(0, 10):
    print(x)
for x in range(10):
    print(x)

for x in range(0, 10, 2):
    print(x)
for x in range(15, 1, -3):
    print(x)

# for loops through lists
my_list = ["abc", 123, "do re mi"]
for i in range(0, len(my_list)):
    print(i, my_list[i])

for v in my_list:
    print(v)

# for loops through dictionaries
my_dict = {"name": "Noelle", "language": "python"}
for k in my_dict:
    print(k)
for k in my_dict:
    print(my_dict[k])

# //////////
capitals ={"Washington":"Olympia","California":"Sacramento", "Idaho":"Boise", "Illinois":"Springfield", "Texas":"Austin", "Oklahoma": "Oklahoma City", "Virginia":"Richmond"}
for key in capitals.keys():
    print(key)

for val in capitals.values():
    print(val)

for key, val in capitals.items():
    print(key, "=", val)

# //////////
capitals ={"Washington":"Olympia","California":"Sacramento", "Idaho":"Boise", "Illinois":"Springfield", "Texas":"Austin", "Oklahoma": "Oklahoma City", "Virginia":"Richmond"}
for key in capitals.keys():
    print(key)

for val in capitals.values():
    print(val)

for full in capitals.items():
    print(key, "=", val)


# while loops
count = 0
while count < 5:
    print("looping -", count)
    count +=1

# else
y = 3
while y > 0:
    print(y)
    y -=1
else:
    print("Final else statement")

# loop control
for val in "string":
    if val == "i":
        break
    print(val)

for val in "string":
    if val == "i":
        continue
    print(val)

    