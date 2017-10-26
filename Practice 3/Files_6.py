""" Файлы 6.
В файле содержится текстовая строка.
Определить частоту повторяемости каждой буквы в тексте и вывести ее.


"""

try :
    fin = open("input.txt", "r")
except FileNotFoundError:
    print("Not find file")

try:
    fout = open("output.txt", "w")
except FileNotFoundError:
    print("Not find file")

myDict = dict()
line = fin.readline()

for symbol in line:
    if not symbol in myDict:
        myDict[symbol] = 1
    elif symbol in myDict:
        myDict[symbol] += 1

for element in myDict:
    fout.write(str(element) + " = " + str(myDict[element]) + "\n")

fin.close()
fout.close()

# try:
#     with open("input.txt", "r") as fin:
#         fin.write("Hello")
#         except FileNotFoundError:
#