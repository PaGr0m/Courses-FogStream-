""" Файлы 6.
В файле содержится текстовая строка.
Определить частоту повторяемости каждой буквы в тексте и вывести ее.

Pavel Gromov
"""

import re

myDict = dict()

try:
    fin = open("input.txt", "r")
except FileNotFoundError:
    print("File not found.")
    exit()

for symbol in fin.readline():
    if re.match(r'[A-Za-zА-Яа-я]', symbol):
        if symbol in myDict:
            myDict[symbol] += 1
        elif not symbol in myDict:
            myDict[symbol] = 1

with open("output.txt", "w") as fout:
    for element in myDict:
        fout.write("{} = {}\n".format(element, myDict[element]))

fin.close()
