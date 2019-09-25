people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = list(map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people)))

if len(heights) > 0:
    import functools
    from operator import add
    average_height = int(functools.reduce(add ,heights) / len(heights))
    
print(average_height) 