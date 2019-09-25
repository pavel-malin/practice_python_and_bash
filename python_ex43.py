import functools
sums = functools.reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])

print(sums)