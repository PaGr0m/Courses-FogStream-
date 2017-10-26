"""

Pavel Gromov
"""

myString = input("Enter the string: ")
myString = list(myString)

i = 0
min = len(myString) + 1
max = -1
while i < len(myString):
    if "f" == myString[i]:
        if min > i:
            min = i
        if max < i:
            max = i
    i = i + 1

if (min == max):
    print(min)
elif (max == -1):
    print (-1)
else:
    print(min, max)