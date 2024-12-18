import random
elem = random.randint (3, 21)
print(elem)
text = ''
for x in range (1, elem):
    for y in range (1, elem):
        if y <= x:
            continue
        if elem % (x + y) ==0:
            text += f'{x}{y}'
print(text)