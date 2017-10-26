""" Функции 6.
Реализовать функцию-валидатор почтовых адресов.
Принимает строку, которая содержит адрес электронной почты.
Возвращает True, если адрес валидный, иначе возвращает False.

Валидным адресом называется такой, который удовлетворяет следующим условиям:
1. Имеет формат username@websitename.extension
2. username может содержать только латинские буквы, целые числа, нижние подчеркивания и тире
3. websitename содержит только латинские буквы и целые числа
4. Максимальная длина extension 3 символа.

Example: grom-razord@mail.ru
Pavel Gromov
"""

checkAlpha = list()
checkDigit = list()
checkSymbol = list()

for el in range(65, 91):
    checkAlpha += chr(el)
for el in range(97, 123):
    checkAlpha += chr(el)
for el in range (48, 58):
    checkDigit += chr(el)

checkSymbol += chr(45) + chr(95)

def validEmail(email):
    #check mail on validator

    userName = email.split("@")[0]
    webSite = email.split("@")[-1].split(".")[0]
    domen = email.split("@")[-1].split(".")[-1]

    if (len(domen) < 4):
        for el in userName:
            if (not el in checkAlpha) and (not el in checkSymbol):
                return False
        for el in webSite:
            if (not el in checkAlpha) and (not el in checkDigit):
                return  False
        return True
    else:
        return False

email = input("Enter mail: ")
print(validEmail(email))