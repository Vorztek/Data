from random import randint

seek_value = randint(0, 1000)

value = int(input("Proposez une valeur entre 0 et 1000 : "))
while value != seek_value:

    if value < seek_value:
        print("Votre valeur est trop basse, réessayez !")
    elif value > seek_value:
        print("Votre valeur est trop haute, réessayez !")

    value = int(input("Proposez une nouvelle valeur : "))

else:
    print("Vous avez trouvé le bon nombre")