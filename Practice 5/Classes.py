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
        # expression = str()
        # degree = self.DEGREE_MAX
        #
        # for element in self.coeffs:
        #     if element >= 0: mark = "+"
        #     else: mark = ""
        #
        #     expression += "{} {}*x^{} ".format(mark, str(element), degree)
        #     degree -= 1
        #
        # return expression
        return str(self.coeffs)

    def __add__(self, other):
        first, second = self.check_length(other)
        result = [0 for tmp in range(len(first))]

        for idx, val in enumerate(first):
            result[idx] = val

        for idx, _ in enumerate(second):
            last_idx = -(idx+1)
            result[last_idx] += second[last_idx]

        return Polynom(result)

    def __sub__(self, other):
        first, second = self.check_length(other)
        result = [0 for tmp in range(len(first))]

        for idx, val in enumerate(first):
            result[idx] = val

        for idx, _ in enumerate(second):
            last_idx = -(idx+1)
            result[last_idx] -= second[last_idx]

        return Polynom(result)

    def __mul__(self, other):
        first, second = self.check_length(other)
        result = [0 for tmp in range(len(first) + len(second) - 1)]
        shift = 0

        for idx, _ in enumerate(second):
            last_idx = -(idx+1)
            last_val = second[last_idx]
            tempList = [0 for tmp in range(len(first))]

            for index, val in enumerate(first):
                last_index = -(index+1)
                tempList[last_index] = val * last_val

            for j, val_tmp in enumerate(tempList):
                last_idx_res = -(shift+j+1)
                result[last_idx_res] += val_tmp

            shift += 1

        return Polynom(result)

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
            return other, self.coeffs
        else:
            return self.coeffs, other


def main():
    a = [1, 2, 3]
    b = [4, 5]

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
