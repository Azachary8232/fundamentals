
#1
def countdown(num):
    list = []
    for x in range(num, -1, -1):
        print(x)
        list.append(x)
    return list        

*newList = countdown(5)
print(newList)

#2
def print_and_return(list):
    print(list[0])
    return(list[1])

print(print_and_return([1,2]))

#3
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([1,2,3,4,5]))

#4
#function that creates a 'New List' with values greater than 2nd value
#print amount of values greater than 2nd
#if list has < 2 elements return False
def values_greater_than_second(list):
    new_list = []
    count = 0
    for i in range(0, len(list)):
        if list[i] > list[1]:
            count = count + 1
            new_list.append(list[i])
    if count < 2:
        return False
    else:
        print(count)
        return new_list           

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5,4,3,2,1,4]))

#5
def length_and_value(length, value):
    new_list = []
    for x in range(length):
        new_list.append(value)
    return new_list

print(length_and_value(4,7))
print(length_and_value(6,2))
