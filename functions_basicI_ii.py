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
"""
#2
def print_and_return(x,y):
    print(x)
    return(y)

print(print_and_return(1,2))