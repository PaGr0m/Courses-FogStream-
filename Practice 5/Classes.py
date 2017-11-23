""" Class

3. Составить описание класса многочленов от одной переменной, задаваемых степенью многочлена и массивом коэффициентов.
Предусмотреть методы для вычисления значения многочлена для заданного аргумента, операции сложения,
вычитания и умножения многочленов с получением нового объекта-многочлена, вывод на экран описания многочлена.

Pavel Gromov
"""


import re

class Polynom():

    def __init__(self, coeffs):
        # if self.check_polynom(coeffs):
        self.coeffs = coeffs
        self.DEGREE_MAX = len(coeffs) - 1
        self.index = -1
        # else:
        #     print("Error")
        #     exit()

    def __len__(self):
        count = 0

        for el in self.coeffs:
            count += 1

        return count

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.coeffs[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1

        return result

    def __repr__(self):
        return self.coeffs

    def __str__(self):
        expression = str()
        degree = self.DEGREE_MAX

        for element in self.coeffs:
            if element != 0:
                if element >= 0: mark = "+"
                else: mark = ""

                expression += "{} {}*x^{} ".format(mark, str(element), degree)
            degree -= 1

        return expression

    def __add__(self, other):
        first, second = self.check_length(other)
        result = [0 for tmp in range(len(first))]

        for first_idx, first_val in enumerate(first):
            result[first_idx] = first_val

        for second_idx, second_val in enumerate(second):
            result[second_idx] += second_val

        return Polynom(result[::-1])

    def __sub__(self, other):
        first, second = self.check_length(other)
        result = [0 for tmp in range(len(first))]

        for first_idx, first_val in enumerate(first):
            result[first_idx] = first_val

        for second_idx, second_val in enumerate(second):
            result[second_idx] -= second_val

        return Polynom(result[::-1])

    def __mul__(self, other):
        first, second = self.check_length(other)
        result = [0 for tmp in range(len(first) + len(second) - 1)]
        shift = 0

        for second_val in second:
            for index, first_value in enumerate(first):
                result[index+shift] += first_value * second_val
            shift += 1

        return Polynom(result[::-1])

    def __truediv__(self, other):
        first, second = self.check_length(other)
        first, second = first[::-1], second[::-1]

        try:
            DIVIDE_COEFF = second[0]
        except IndexError:
            print("Один из многочленов пустой")
            DIVIDE_COEFF = 0

        FIRST_INDEX = 0
        shift = 0
        result = []

        for _ in first:
            if DIVIDE_COEFF != 0: tmp = first[FIRST_INDEX] / DIVIDE_COEFF
            else: tmp = 0

            if (tmp != 0): result.append(tmp)
            else: break

            for second_index, second_val in enumerate(second):
                first[second_index] -= tmp * second_val
            first.pop(0)

            shift += 1

        return Polynom(result)

    def __mod__(self, other):
        first, second = self.check_length(other)
        first, second = first[::-1], second[::-1]

        try:
            DIVIDE_COEFF = second[0]
        except IndexError:
            print("Один из многочленов пустой")
            DIVIDE_COEFF = 0

        FIRST_INDEX = 0
        shift = 0
        result = []

        for _ in first:
            if DIVIDE_COEFF != 0: tmp = first[FIRST_INDEX] / DIVIDE_COEFF
            else: tmp = 0

            if (tmp != 0): result.append(tmp)
            else: break

            for second_index, second_val in enumerate(second):
                first[second_index] -= tmp * second_val
            first.pop(0)
            shift += 1

        return Polynom(first)

    def __divmod__(self, other):
        first, second = self.check_length(other)
        first, second = first[::-1], second[::-1]

        try:
            DIVIDE_COEFF = second[0]
        except IndexError:
            print("Один из многочленов пустой")
            DIVIDE_COEFF = 0

        FIRST_INDEX = 0
        shift = 0
        result = []

        for _ in first:
            if DIVIDE_COEFF != 0: tmp = first[FIRST_INDEX] / DIVIDE_COEFF
            else: tmp = 0

            if (tmp != 0): result.append(tmp)
            else: break

            for second_index, second_val in enumerate(second):
                first[second_index] -= tmp * second_val
            first.pop(0)

            shift += 1

        return Polynom(result), Polynom(first)

    def __getitem__(self, index):
        return self.coeffs[index]

    def __setitem__(self, index, value):
        self.coeffs[index] = value

    def check_length(self, other):
        """
        Функция проверяет длины коэф. полиномов.
        :param other: второй полином
        :return: значения полиномов меняются местами (иначе остаются на месте)
                и передаются в обратном порядке для вычислений
        """

        if len(self.coeffs) < len(other):
            return other[::-1], self.coeffs[::-1]
        else:
            return self.coeffs[::-1], other[::-1]

    # def check_polynom(self, coeffs):
    #     for el in coeffs:
    #         print(el)
    #         if re.search(r'[^0-9.]', el):
    #             return False
    #     return True

def main():
    a = [1, 2, 3]
    b = [4, 5]
    # a = ["a"]
    # b = ["b"]
    # a = [4, 5]
    # b = [1, 2, 3]

    poly1 = Polynom(a)
    poly2 = Polynom(b)

    print("Polynom 1 = ", poly1)
    print("Polynom 2 = ", poly2)

    # сложение полиномов
    sum = poly1 + poly2
    print("\nSum: ", sum)

    # разность полиномов
    substract = poly1 - poly2
    print("\nSubstract: ", substract)

    # произведение полиномов
    multiply = poly1 * poly2
    print("\nMultiply: ", multiply)

    # целочисленное деление
    div = poly1 / poly2
    print("\nDiv: ", div)

    # остаток от деления
    remainder = poly1 % poly2
    print("\nRemainder: ", remainder)

    # целая часть от деления и остаток "divmod()"
    divmodPoly = divmod(poly1, poly2)
    print("\nDivmod:\n    Whole: {}\n    Remainder: {}".format(divmodPoly[0], divmodPoly[1]))


if __name__ == "__main__":
    main()
