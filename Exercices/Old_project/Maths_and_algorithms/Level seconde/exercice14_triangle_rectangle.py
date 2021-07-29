a, b, c = input("Entrer les valeurs de a, b, et c : ").split()
a = int(a)
b = int(b)
c = int(c)

if (a**2) + (b**2) == c ** 2:
    print('Vrai')
else:
    print('Faux')