"""

Pavel Gromov
"""

myString = list(input("Enter the string: "))

i = 0
result = str("")

while len(myString) > 0:
    if myString[0] == "1":
        result = result + "one"
    else:
        result = result + myString[0]
    myString.pop(0)
    print(myString)
print (result)