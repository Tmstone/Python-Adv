# update dictionaries and lists

x = [[5,2,3],[10,8,9]]
x[1][0] = 15
print(x)

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball': ['Kobe','Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [{'x': 10, 'y':20}]
z[0]['y'] = 30
print(z)

# Itereate through a list of directories
def itererateDictionary(some_dict):
    for some_dict in students:
        print('first_name - ' + some_dict['first_name'] + ", " + 'last_name - ' + some_dict['last_name'])


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan' },
    {'first_name': 'John', 'last_name': 'Rosales' },
    {'first_name': 'Mark', 'last_name': 'Guillen' },
    {'first_name': 'KB', 'last_name': 'Tonel' }
    ]
itererateDictionary(students)

#Get Values from a list of dictionaries
#Parameters take two values
def itererateDictionary2(key_name, some_list):
    print('\n')
    for student in some_list:
        print(student[key_name])

itererateDictionary2('first_name', students) #this still needs work
itererateDictionary2('last_name', students)
print()

#Itereate through a dictionary with List Values
def printInfo(dojo_dict):
    #counting the items in each list
    city_count = len(dojo_dict['locations'])
    teach_count = len(dojo_dict['instructors'])

    print(city_count, ' LOCATIONS')
    #iterating through the locations list
    for place in dojo_dict['locations']:
        print(place)

    print(teach_count, ' INSTRUCTORS')
    #iterating through the instructors list
    for teachers in dojo_dict['instructors']:
        print(teachers)

    #first attampt to print the items in the dictionary using a nested list
    #for place, things in dojo_dict.items():
    #    print(place.title())
    #    for cities in things:
    #        print(cities.title())

dojo = {
    'locations': ['San Jose','Seatle','Dallas','Chicago','Tulsa','DC','Burbank'],
    'instructors': ['Michael','Amy','Eduardo','Josh','Graham','Patrick','Minh','Devon']
    }

printInfo(dojo) # this needs to print the number
