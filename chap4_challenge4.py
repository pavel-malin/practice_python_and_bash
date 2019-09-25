# two functions, division and multiplication by 2
namebers = input("number: ")
namebers = int(namebers)

def odd():
    a = namebers // 2
    return a


def number():
    a = namebers * 2
    return a

print(odd())
print(number())
