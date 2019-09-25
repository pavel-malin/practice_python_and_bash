import functools

sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

sam_count = functools.reduce(lambda a, x: a + x.count('Sam'),
                             sentences, 0)

print(sam_count)