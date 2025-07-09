# ul Composite types
#  li lists
empty_list = []
ninjas  = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

# li Dictionaries
empty_dict = {}
new_person = {'name':'John', 'age': 38, 'weight':160.2, 'has_glasses':False}
new_person['name'] = 'Jack'
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
w = new_person.pop('weight')
print(w)
print(new_person)

# ul Commen Functions

# li type
print(type(896.364))
print(type(new_person))
print(type(ninjas))

# li len
print(len(new_person))
print(len('Mahmoud Shuman'))

# ul Type Casting or Explict Type Conversion

# li str
# print("Hello" + 42)
print("Hello" + " " + str(42))

# li int
total = 35
user_val = "26"
# total = total + user_val
total = total + int(user_val)
print(total)
