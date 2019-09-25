filename = 'username.txt'
r = input("You name?: ")

with open(filename, 'w') as f:
    f.write(r)

with open(filename, 'r') as f:
    print(f.read())

# Similarly csv

import csv

filename = 'username.csv'
r = input('You name?: ')

with open(filename, 'w') as f:
    w = csv.writer(f)
    w.writerow(r)

with open(filename, 'r') as f:
    a = csv.reader(f)
    for aa in a:
        print("".join(aa))
