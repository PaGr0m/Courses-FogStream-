checkAlpha = list()
checkDigit = list()
checkSymbol = list()

for el in range(65, 91):
    checkAlpha += chr(el)
for el in range(97, 123):
    checkAlpha += chr(el)

for el in range (48, 58):
    checkDigit += chr(el)

checkSymbol += chr(45)
checkSymbol += chr(95)

def validEmail(email):
    userName = email.split("@")[0]
    webSite = email.split("@")[-1].split(".")[0]
    domen = email.split("@")[-1].split(".")[-1]

    print("User: ", userName)
    print("Website: ", webSite)
    print("Domen: ", domen)

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