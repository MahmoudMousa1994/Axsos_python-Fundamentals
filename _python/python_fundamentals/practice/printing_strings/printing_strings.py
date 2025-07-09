print("this is a sample string")
name = "zen"
print("My name is", name)
print("My name is "+ name)

first_name = "zen"
last_name = "coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
hw = "Hello %s" % "world"
py = "I love python %d" % 3
print(hw, py)
print("My name is %s and I'm %d" % (name, age))
x = "hello world I am Mahmoud"
print(x.count("l"))
print(x.split(" "))
print(x.find("a"))
print(name.isalnum())
print(x.isalnum())
print(name.isalpha())
print(x.isalpha())
print(name.isdigit())
print(x.isdigit())
print(last_name.islower())
m = ["MJ","MHD","MJM"]
print("\n".join(m))
print(x.endswith("Mahmoud"))


