"""
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
"""
#3
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([1,2,3,4,5]))