"""
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys

Pavel Gromov
"""
import os

path = input("Enter the path: ")

myDir = os.listdir(path)

print(myDir)