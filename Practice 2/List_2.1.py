""" Списки 2.
Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.

Pavel Gromov
"""

lst = list(int(input("Enter the numbers: ").split()))
lst = list(map(int, lst))
myList = list()

if (len(lst) > 1):
    for index in range(0, len(lst) - 1):
        if ((lst[index] > 0 and lst[index + 1] > 0) or
                (lst[index] < 0 and lst[index + 1] < 0)):
            myList.append([lst[index], lst[index + 1]])
    print(myList[0])
