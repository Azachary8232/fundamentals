
#1
for x in range(151):
    print(x)

#2
for x in range(5,151,5):
    print(x)

#3
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 10 != 0 and x % 5 == 0:
        print("Coding")
    else:
        print(x)

#4
sum = 0
for x in range(1,500001,2):
    sum += x
print(sum)

#5
for x in range(2018, 0, -4):
    print(x)



