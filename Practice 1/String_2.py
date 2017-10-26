"""
2.Дана строка.
Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина первой части должна быть на один символ больше).
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

Pavel Gromov
"""

myString = input("Enter the string \n")

if len(myString)%2 == 0:
    middleString = len(myString)//2
else:
    middleString = len(myString)//2 + 1

reverseString = myString[middleString:] + myString[:middleString]
print(reverseString)