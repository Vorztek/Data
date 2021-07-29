entier = list(range(0, 2013))
entier2 = []
entier3 = 0
for i in entier:
    if i % 5 == 0 or i % 7 == 0:
        entier2.append(i)


print(sum(entier2))

