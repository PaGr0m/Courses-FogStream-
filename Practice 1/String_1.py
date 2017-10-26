"""
1.Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
"""

myText = input("Enter the text \n")
count = 0

for word in myText.split(" "):
    count = count + 1

print("Count if words = ", count)