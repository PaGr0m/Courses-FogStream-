# lst = list(input("Enter the numbers"))

lst = [1, -2, 2, -3, -23]

flagCheck = False

for index in range(0, len(lst) - 1):
    if not flagCheck:
        if ((lst[index] > 0 and lst[index + 1] > 0) or (lst[index] < 0 and lst[index + 1] < 0)):
            result = [lst[index], lst[index + 1]]
            flagCheck = True

if flagCheck:
    print (result)
