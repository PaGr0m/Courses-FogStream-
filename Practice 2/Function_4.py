""" Функции 4.
Дан список результатов попыток одного спортсмена для некоторого соревнования.
Написать функцию, которая считает сколько за сессию был установлен новый рекорд,
т.е. текущее значение превышает значение максимального.

Например
Имеем список результатов.:
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1].
В данном случае ответ: 2.

Pavel Gromov
"""

def checkScore(lst):
    maxScore = list_of_scores[0]
    count = 0

    for score in list_of_scores:
        if score > maxScore:
            maxScore = score
            count += 1

    return count

list_of_scores = list(input("Enter scores: ").split())
list_of_scores = list(map(int, list_of_scores))

print(checkScore(list_of_scores))
