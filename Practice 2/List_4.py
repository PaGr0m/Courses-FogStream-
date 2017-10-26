""" Списки 4.
Найти все уникальные элементы в списке.
Список произвольной длины и может состоять как из чисел, так и строк.

Pavel Gromov
"""

lst = input("Enter the list: ").split()
lst = list(map(str, lst))
myDict = dict()

for element in lst:
    if not element in myDict:
        myDict[element] = 0
    elif element in myDict:
        myDict[element] += 1

for myKey in myDict:
    if myDict[myKey] == 0:
        print(myKey)
