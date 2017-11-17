"""
3. Составить описание класса многочленов от одной переменной, задаваемых степенью многочлена и массивом коэффициентов.
Предусмотреть методы для вы­числения значения многочлена для заданного аргумента, операции сложения,
вычитания и умножения многочленов с получением нового объекта-многочлена, вывод на экран описания многочлена.


"""


class Polynom():

    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.DEGREE_MAX = len(coeffs) - 1
        self.idx = 0

    def __len__(self):
        count = 0

        for el in self.coeffs:
            count += 1

        return count

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.coeffs[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1

        return result

    def __repr__(self):
        return self.coeffs

    def __str__(self):
        expression = str()
        degree = self.DEGREE_MAX

        for element in self.coeffs:
            if element >= 0: mark = "+"
            else: mark = "-"

            expression += "{} {}*x^{} ".format(mark, str(element), degree)
            degree -= 1

        return expression

    def __add__(self, other):
        other = self.check_length(other)

        for idx, _ in enumerate(other):
            last_idx = -(idx+1)
            self.coeffs[last_idx] += other[last_idx]

        return Polynom(self.coeffs)

    def __sub__(self, other):
        other = self.check_length(other)

        for idx, _ in enumerate(other):
            last_idx = -(idx+1)
            self.coeffs[last_idx] -= other[last_idx]

        return Polynom(self.coeffs)

    def __mul__(self, other):
        other = self.check_length(other)

        for idx, _ in enumerate(other):
            last_idx = -(idx+1)
            self.coeffs[last_idx] *= other[last_idx]

        return Polynom(self.coeffs)

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
        if len(self.coeffs) < len(other):
            self.coeffs, other = other, self.coeffs

        return other


def main():
    a = [5, 7, 2, 4, -8]
    b = [-8, 1, 13, 1]
    c = [1, 2]

    poly1 = Polynom(a)
    poly2 = Polynom(b)
    poly3 = Polynom(c)

    print("Polynom 1 = ", poly1)
    print("Polynom 2 = ", poly2)
    print("Polynom 3 = ", poly3)

    summa = poly1 + poly2 * poly3

    print("\nSumma: ", summa)


if __name__ == "__main__":
    main()
