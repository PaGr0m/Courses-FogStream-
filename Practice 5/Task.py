""" Class 3
Требуется записать в файл input.txt коэффициенты многочлена от одной переменной.
Каждая строка - новый многочлен.
В файл output.txt записывается сумма, разность, произведение, частное и остаток от деления данных многочленов.

Pavel Gromov
"""


import Classes
import os
import re


def check_input(file):
    for line in file.readlines():
        for symbol in line:
            if re.search(r'[^0-9 .\n]', symbol):
                file.seek(0)
                return False
    file.seek(0)
    return True


def main():
    try:
        fin = open("input.txt", "r")
    except FileNotFoundError:
        print("File not found")
        exit()


    if os.stat("input.txt").st_size != 0 and check_input(fin):
        result_sum = Classes.Polynom([0])
        result_sub = Classes.Polynom([0])
        result_mul = Classes.Polynom([1])

        div_flag = True

        for line in fin.readlines():
            tmp_poly = []

            for element in line.split():
                tmp_poly.append(float(element))

            result_sum += Classes.Polynom(tmp_poly)
            result_sub -= Classes.Polynom(tmp_poly)
            result_mul *= Classes.Polynom(tmp_poly)

            if div_flag:
                result_div = Classes.Polynom(tmp_poly)
                result_rem = Classes.Polynom(tmp_poly)
                div_flag = False
            else:
                result_div /= Classes.Polynom(tmp_poly)
                result_rem %= Classes.Polynom(tmp_poly)

        fin.close()
        outputList = ("Sum", "Substraction", "Multiplication", "Integer division", "Remainder of the division")
        outputResult = (result_sum, result_sub, result_mul, result_div, result_rem)

        with open("output.txt", "w") as fout:
            for el, val in enumerate(outputList):
                fout.write("{} = {}\n".format(val, outputResult[el]))
    else:
        print("File is empty or incorrect input")


if __name__ == '__main__':
    main()