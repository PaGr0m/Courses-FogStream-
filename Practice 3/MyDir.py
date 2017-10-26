"""
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys

Pavel Gromov

/home/pagrom/Рабочий стол/Test

"""

import os
import re

def countDir(path):
    return len(re.findall(r'/', path))

def checkDir(path):

    for element in os.listdir(path):
        tmpPath = path + "/" + element

        if (os.path.isfile(tmpPath)):
            print("-" * countDir(tmpPath), element)

        if (os.path.isdir(tmpPath)):
            print("-" * countDir(tmpPath), element)
            checkDir(tmpPath)

path = input("Enter the path: ")

try:
    print(path, ":")
    checkDir(path)
except FileNotFoundError:
    print("Файл или директория не существуют")
except NotADirectoryError:
    print("Ожидалась директория, но это файл")
