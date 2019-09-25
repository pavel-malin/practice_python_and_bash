import csv

with open('st.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['one', 'two', 'three'])
    w.writerow(['four', 'five', 'six'])

with open('st.csv', 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(",".join(row))