sentences = ['Mary read a story to Sam and Isla',
             'Isla cuddled Sam.',
             'Sam chortled.']

sam_count = 0
for sentence in sentences:
    sam_count += sentence.count('Sam')

print(sam_count)