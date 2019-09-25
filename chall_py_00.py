import re

t = open('zen.txt')
file = t.read()

found = re.findall("be", file, re.IGNORECASE)
pir = re.findall('python', file, re.IGNORECASE)

print(found)
print(len(found))

print(pir)
print(len(pir))

