#1
def countdown(num):
    list = []
    for x in range(num, -1, -1):
        print(x)
        list.append(x)
    return list        

*newList = countdown(5)
print(newList)