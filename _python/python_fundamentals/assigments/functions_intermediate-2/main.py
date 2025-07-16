# A- Ubdate values in dictionaries and lists
x = [[5,2,3],[10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'}
]
sprts_directory = {
    'basketball':['Kobe','Jordan','James','Curry'],
    'football' :['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x':10,'y':20}]

# A-1.change the value 10 in x to 15
x[1][0] = 15
print(x)

# A-2. change the last name of the first student from jordan to Bryant
students[0]['last_name']= 'Bryant'
print(students[0])

# A-3. change Messi to Andres
sprts_directory['football'][0]='Anders'
print(sprts_directory['football'])

# A-4.change the value 20 in z to 30
z[0]['y']= 30
print(z)

# //////////////////////////////////////

# B-Iterate througha list of dictionaries

students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'},
    {'first_name' :'Mark' , 'last_name' : 'Guillen'},
    {'first_name' :'KB' , 'last_name' : 'Tonel'}
]
def iterateDictionary(x):
    for player in x:
        print(f"first_name - {player['first_name']}, last_name - {player['last_name']}")
iterateDictionary(students)

# C- get valuse from a list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'},
    {'first_name' :'Mark' , 'last_name' : 'Guillen'},
    {'first_name' :'KB' , 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name,x):
    for player in x:
        print(player[key_name])


iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# D- iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose','Seattle','Dalas','Chicago','Tulsa','DC','Burbank'],
    'instructors':['Michael','Amy','Eduardo','Josh','Graham','Patrick','Minh','Devon']
}
def printInfo(x):
    for key in x:
        print(len(x[key]),key.upper())
        for val in x[key]:
            print(val)
printInfo(dojo)