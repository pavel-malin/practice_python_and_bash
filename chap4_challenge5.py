# check whether conducted float, int, number,  not string
try:
    f = input()
    print(float(f))
except ValueError:
    print(f + " Sorry, not float")
