""" Списки 2.
Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.

Pavel Gromov
"""

lst = list(input("Enter the numbers: ").split())
lst = list(map(int, lst))
myList = list()

lst = list(zip(lst[:-1], lst[1:]))

for first, second in lst:
    if ((first > 0) and (second > 0)) or ((first < 0) and (second < 0)):
        myList.append([first, second])

if len(myList) != 0:
    print(myList[0])
