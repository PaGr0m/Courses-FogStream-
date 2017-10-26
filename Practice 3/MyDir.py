"""
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys

Pavel Gromov

/home/pagrom/Рабочий стол/Test

"""

import os

def checkDir(path, count):
    for element in os.listdir(path):
        if (os.path.isfile(path + "/" + element)):
            print("-" * count, element)
        if (os.path.isdir(path + "/" + element)):
            print("-" * count, element)
            count += 5
            checkDir(path + "/" + element, count)

path = input("Enter the path: ")
count = 5
try:
    checkDir(path, count)
except FileNotFoundError:
    print("Файл или директория не существуют")
except NotADirectoryError:
    print("Ожидалась директория, но это файл")
