def conway(n):
    sequence = [1]
    for _ in range (n-1):
        suivant = []
        for i in sequence:
            if not suivant or suivant[-1] != i:
                suivant += (1, i)
            else:
                suivant[-2] += 1

        sequence = suivant

    return "".join(map(str, sequence))


def affichage(n):
    for i in range(0, n):
        print(conway(i))


affichage(10)

