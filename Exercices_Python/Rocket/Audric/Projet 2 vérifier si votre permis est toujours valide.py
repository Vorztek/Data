#Projet 2 vérifier si votre permis est toujours valide

print("Combien de stop avez vous grillé ?")
s = input()
print("Combien de feux rouges avez vous grillé ?")
f = input()
print("Combien de fois vous avez oublié votre ceinture ?")
c = input()
print("Combien de fois étiez-vous au dessus du taux d'alcoolémie autorisé")
a = input()


number_first = 12
stop = 3 * s
exces_vitesse = 2 * f
ceinture = 1 * c
alcool = 3 * a
number_second = stop + exces_vitesse + ceinture + alcool
if number_first >= int(number_second):
   print("Vérification de la validité de votre permis : Toujours en cours")
else:
   print("Bien joué pilote, tu n'as plus de permis")
