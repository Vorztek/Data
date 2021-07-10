nb1 = int(input("Veuillez entrer un premier nombre entier : "))
nb2 = int(input("Veuillez entrer un second nombre entier : "))
reste = 8

while reste != 0:
    nb1 / nb2
    reste = nb1 % nb2
    if reste == 0:
        print("Le PGCD de vos deux nombres est {}".format(nb2))
        break
    else:
        nb1 = nb2
        nb2 = reste

