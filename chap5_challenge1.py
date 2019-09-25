lists = ['hello', 'vvv', 'www', 'aaa', 111, 2424, 'was', 'bin']

tuples = ('go', 'me', 11, 242, 545)

p = {
    'will': 12,
    'qqq': 'wwwewe',
    '111': '222',
}



n = input('name: ')
if n in p:
    p = p[n]
    print(p)
else:
    print('Error')

print(a)