# TP9 Utilisons des fonctions pour calculer les coûts de votre voyage:¶
# - Définissez une fonction appelée hotel_cost avec un argument nuits comme entrée. L'hôtel coûte 140€ par nuit. Ainsi, la fonction hotel_cost devrait renvoyer 140 * nuits.
# - Définissez une fonction appelée plane_ride_cost qui prend en entrée une chaîne city. La fonction doit renvoyer un prix différent selon l'emplacement, similaire à l'exemple de code ci-dessous. Vous trouverez ci-dessous les destinations valides et leurs tarifs aller-retour correspondants.
# "Paris": 183, "Lyon": 220, "Marseille": 222 ,"Surfers Paradise": 475
# -Sous votre code existant, définissez une fonction appelée rental_car_cost avec un argument appelé jours. Calculez le coût de la location de la voiture: Chaque jour, vous louez la voiture coûte 40€. (Coût = 40 * jours) si vous louez la voiture pour 7 jours ou plus, vous obtenez 50€ de réduction sur votre total (coût- = 50). Alternativement (elif), si vous louez la voiture pour 3 jours ou plus, vous obtenez 20€ de réduction sur votre total. Vous ne pouvez pas bénéficier des deux réductions en même temps. Renvoyez ce coût puis, définissez une fonction appelée trip_cost qui prend deux arguments, ville et jours. Demandez à votre fonction de renvoyer la somme des fonctions rental_car_cost (jours), hotel_cost (jours) et plane_ride_cost (ville).
# - Modifiez la fonction trip_cost avec. Ajoutez un troisième argument, spending_money. Modifiez ce que fait la fonction trip_cost. Ajoutez la variable "spending_money" à la somme qu'elle renvoie.

#data

city = {"Paris": 183, "Lyon": 220, "Marseille": 222 ,"Surfers Paradise": 475}

#Fonction hotel_cost, qui renvoie le coût de l'hotel en fonction de nb jours

def hotel_cost(jours):
      return 140 * jours

#renvoie le coût selon la ville

def plane_ride_cost(city_name):
      new_value = city[city_name]
      return new_value

#renvoie le coûts de la location du véhicule selon nb jours avec la réduc

def rental_car_cost(jours):
   if jours > 7:
      rental_new_value = (40 * jours) - 50
   elif jours > 3:
      rental_new_value = (40 * jours) - 20
   else:
      rental_new_value = 40 * jours
   return rental_new_value

#renvoie la somme des fonctions précédentes + spending money à la fin

def trip_cost(jours, city_name, spending_money):
    trip_cost = hotel_cost(jours) + plane_ride_cost(city_name) + rental_car_cost(jours) + spending_money
    return trip_cost

#affiche trip cost avec les 3 arguments

print(trip_cost(6, "Marseille", 200))