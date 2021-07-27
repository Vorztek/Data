liste_1 = ["a", "b"]
liste_2 = [1, 2]

def list_to_dict(liste_1, liste_2):

    dictionnaire = dict()
    for i in range(len(liste_1)):
        dictionnaire[liste_1[i]] = liste_2[i]
        return dictionnaire

list_to_dict(liste_1, liste_2)

# inverser les chiffres d'un nombre : 
#https://www.youtube.com/watch?v=GCYoabTaBjs&list=PL6JtJ0Q7T-YwoXY5PletTK9ITQ8YPDa-G&index=58