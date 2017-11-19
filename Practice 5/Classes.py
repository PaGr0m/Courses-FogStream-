""" Class

3. Составить описание класса многочленов от одной переменной, задаваемых степенью многочлена и массивом коэффициентов.
Предусмотреть методы для вычисления значения многочлена для заданного аргумента, операции сложения,
вычитания и умножения многочленов с получением нового объекта-многочлена, вывод на экран описания многочлена.

Pavel Gromov
"""


class Polynom():

    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.DEGREE_MAX = len(coeffs) - 1
        self.index1 = -1

    def __len__(self):
        count = 0

        for el in self.coeffs:
            count += 1

        return count

    def __iter__(self):
        return iter(self.coeffs)
        # return self

    def __next__(self):
        try:
            result = self.coeffs[self.index1]
        except IndexError:
            raise StopIteration

        self.index1 -= 1

        return result

    def __repr__(self):
        return self.coeffs

    def __str__(self):
        expression = str()
        degree = self.DEGREE_MAX

        for element in self.coeffs:
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
        other = self.check_length(other)

        for idx, _ in enumerate(other):
            last_idx = -(idx+1)
            try:
                self.coeffs[last_idx] /= other[last_idx]
            except ZeroDivisionError:
                print("Деление на 0")
                exit()

        return Polynom(self.coeffs)

    def __getitem__(self, index):
        return self.coeffs[index]

    def __setitem__(self, index, value):
        self.coeffs[index] = value

    def check_length(self, other):
        if len(self.coeffs) < len(other.coeffs):
            return other[::-1], self.coeffs[::-1]
        else:
            return self.coeffs[::-1], other[::-1]


def main():
    # a = [1, 2, 3]
    # b = [4, 5]

    a = [4, 5]
    b = [1, 2, 3]

    poly1 = Polynom(a)
    poly2 = Polynom(b)

    print("Polynom 1 = ", poly1)
    print("Polynom 2 = ", poly2)

    sum = poly1 + poly2
    print("\nSumma: ", sum)

    substract = poly1 - poly2
    print("\nSubstract: ", substract)

    multiply = poly1 * poly2
    print("\nMultiply: ", multiply)


if __name__ == "__main__":
    main()
