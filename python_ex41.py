import random

names = ['Mary', 'Isla', 'Sam']

secret_names = map(lambda x: random.choice(['Mr.Pink',
                                            'Mr.Orange',
                                            'Mr.Blonde']), 
                   names)

print(list(secret_names))