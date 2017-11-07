""" Final 1
3.Дан файл с каким-то математическим выражением, которое содержит скобки разных типов “{[()]}” в любом порядке.
Проверить сбалансированны ли скобки.
В случае сбалансированности вывести результат вычисления выражения, иначе вывести сообщение об ошибке.

Pavel Gromov
"""

def checkInput(text):
    """
    Проверка ввода
    :param text: строка из файла
    :return: True/False
    """

    checkList = "0123456789(){}[]+-*/"

    if text:
        for symbol in text:
            if not symbol in checkList:
                return False
        return True
    else:
        return False


def isBalanced(text):
    """
    Проверка на сбалансированность
    :param text: строка из файла
    :return: true/false
    """

    open_parenthesis = "([{"
    close_parenthesis = ")]}"
    stack = []
    last_index = -1

    for symbol in text:
        if symbol in open_parenthesis:
            stack.append(open_parenthesis.index(symbol))
        elif symbol in close_parenthesis:
            if stack and stack[last_index] == close_parenthesis.index(symbol):
                stack.pop()
            else:
                return False
    return (not stack)


def transformationExpression(line):
    """
    Преобразование всех скобок на круглые
    :param line: строка из фала
    :return: преобразованная строка
    """

    expression = str()

    for symbol in line:
        if symbol == "{" or symbol == "[":
            expression += "("
        elif symbol == "}" or symbol == "]":
            expression += ")"
        else:
            expression += symbol
    return expression


def main():
    try:
        fin = open("input.txt", "r")
    except FileNotFoundError:
        print("File not found.")
        exit()

    line = fin.readline()
    fin.close()

    if checkInput(line) and isBalanced(line):
        try:
            result = eval(transformationExpression(line))
        except ZeroDivisionError:
            print("Error: Division by zero")
            exit()
        except TypeError:
            print("Error: Object is not callable")
            exit()
        except SyntaxError:
            print("Error: Syntax")
            exit()

        with open("output.txt", "w") as fout:
            fout.write(str(result))
    else:
        print("Expression is not balanced or Error input")

if __name__ == "__main__":
    main()
