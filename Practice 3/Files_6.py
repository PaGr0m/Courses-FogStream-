""" Файлы 6.
В файле содержится текстовая строка.
Определить частоту повторяемости каждой буквы в тексте и вывести ее.

"""

import re

myDict = dict()

try:
    fin = open("input.txt", "r")
except FileNotFoundError:
    print("File not found.")

# for line in fin.readlines():
for symbol in fin.readline():
    if re.match(r'[A-Za-zА-Яа-я]', symbol):
        if symbol in myDict:
            myDict[symbol] += 1
        elif not symbol in myDict:
            myDict[symbol] = 1

with open("output.txt", "w") as fout:
    for element in myDict:
        # fout.write(str(element) + " = " + str(myDict[element]))
        fout.write("{} = {}\n".format(element, myDict[element]))
