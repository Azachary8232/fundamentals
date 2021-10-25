
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z[0])

#2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list):
    for x in range(0, len(list)):
        print(list[x])

iterate_dictionary(students)    

#3
def iterate_dictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        print(some_list[x][key_name])

iterate_dictionary2('first_name', students)    
iterate_dictionary2('last_name', students)    

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info2(some_dict2):
    for key in some_dict2:
        print(len(some_dict2[key]), key.upper())
        for items in some_dict2[key]:
            print(items)
        print()

print_info2(dojo)














