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

listAlpha = list()
listDigit = list()
listSymbol = list()
listUsername = list()
listWebsite = list()

for el in range(65, 91): listAlpha += chr(el)
for el in range(97, 123): listAlpha += chr(el)
for el in range (48, 58): listDigit += chr(el)

listSymbol += chr(45) + chr(95)
listUsername += listAlpha + listDigit + listSymbol
listWebsite += listAlpha + listDigit

def checkUsername(str):
    for el in str:
        if not el in listUsername:
            return False
    return True

def checkWebsite(str):
    for el in str:
        if not el in listWebsite:
            return False
    return True

def checkDomen(str):
    if (len(str) > 3):
        return False
    return True

def validEmail(email):
    #check mail on validator

    userName = email.split("@")[0]
    webSite = email.split("@")[-1].split(".")[0]
    domen = email.split("@")[-1].split(".")[-1]

    # print("User: ", userName)
    # print("Website: ", webSite)
    # print("Domen: ", domen)

    if (len(domen) < 4):
        if (checkUsername(userName) and
              checkWebsite(webSite) and
                checkDomen(domen)):
            return True
        else:
            return False
    else:
        return False

email = input("Enter mail: ")
print(validEmail(email))