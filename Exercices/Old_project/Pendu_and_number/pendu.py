import random 

def word():
    global choice
    global nb_letter
    #nb_letter = int(input("Combien de lettres souhaitez-vous dans votre mot ? : "))
    nb_letter = 10
    with open(r"C:\Users\vion1\Ele\Engie\Exercices_Python\Mini_project\liste_francais.csv") as fichier:  
        lists_from_csv = (fichier.read()).split() #Lire le fichier et en faire une liste propre (sans qu'elle soit à l'intérieur d'une liste)
        new_list = [x for x in lists_from_csv if len(x) == nb_letter] #Recréer une liste avec la condition du nombre de lettre
        choice = random.choice(new_list) #Choisis un mot au hasard parmi la bonne lettre. OMG ça marche et c'est propre (5h de travail bordel ?)
        return choice
        
print(word())

def asking():
    dictionnaire = {1: 0}
    test = input("Quelle lettre souhaitez-vous tester ? : ")
    upper_test = test.upper()
    upper_choice = choice.upper()
    print("Le mot est {}".format(list(upper_choice))) 
    #en fait cette partie là fonctionne directement sous forme de liste,
    #pas besoin du dictionnaire (que je dois quand même à priori utiliser pour stocker les données)

    for i in range (nb_letter):
        dictionnaire[i] = "_"
    print("Le mot est {}".format(list(dictionnaire.values())))


print(asking())

#à finir un jour peut-être