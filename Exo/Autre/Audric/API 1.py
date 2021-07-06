# # # 1 . Code de la requête
# # # Le mlot clé import est nécessaire pour utiliser un module. Vous de vez l'importer avant de pouvoir l'utiliser
# #
# # import requests
# #
# # #Requête pour obtenir la dernière position de la station spaciale
# # # URL : http://api.open-notify.org/iss-now.json
# # # Verbes HTTPS : Getr/Post/Deleted
# # flux_logique_de_la_patate = requests.get("http://api.open-notify.org/iss-now.json") #404 si erreur, le serveur n'a pas trouvé la ressource. Erreur d'URL
# #
# # #Récupérer le code status
# # #Indique comment s'est passé la requête
# # # 200 -  Tout s'est bien passé, le résultat est dispo
# #
# # flux_logique_de_la_patate #Fonctionne pas !!!
# #
# # # Afficher proprement le code de status de la requête get
# #
# # status_code = flux_logique_de_la_patate.status_code
# # print(status_code)
# #
# # # 2 . Paramètre de la requête
# #
# # # M'envoyer les informations de l'API de l'ISS en fonction de ma position
# # # Pour utiliser cette API vous devez obligatoirement préciser les paramètres
# # # Chez moi : 48°54'51.3"N 2°14'56.5"E
# # parameters = {"lat": 48.54, "long" : 2.14}
# #
# # # Ajouter les paramètres dans la requête get
# #
# # flux_logique_de_la_patate = requests.get("http://api.open-notify.org/iss-now.json", params = parameters ) #passer un argument
# #
# # # Récupérer le contenu de l'API
# #
# # content = flux_logique_de_la_patate.content
# #
# # print(content)
#
# # 3 . Format JSON
#
# # dumps
# # Prendre en entrée un object Python et retourner une chaine de caractères
# # loads
# # Prendre en entrée une chaine de caractères (json) et retourner des listes
#
# sports = ["Tennis", "Foot", "Golf"]
# print(type(sports))
#
# import json
#
# # Convertir en chaine de caractères
# # Pour utiliser la foncitonnalité u module on utilise un "."
# sports2 = json.dumps(sports)
#
# # Exemple de loads
# print(type(sports2))
#
# sports3 = json.loads(sports2)
# print(type(sports3))


import json
import requests
parameters = {"lat" : 38.89, "lon": -77.03}
response = requests.get("http://api.open-notify.org/iss-now.json", params = parameters )

#Obtenir un object
json.data = response.json() #transforme au format json du module requests
print(type(json.data))

response = requests.get("http://api.open-notify.org/iss-now.json?")
json_data = response.json()

content = response.content
print(content)
print(json_data)

#Récuperer la première valeur de la clé duration : result 384
duration = json_data["iss_position][0])

request = json_data["request"]
request_2 = json_data["request"][2]["latitude"]

#On peut utiliser l'index de position dans une liste mais pas dans un dictionnaire où il faut indiquer le nom de la clé

print(response) #Code de status de la requête

#En savoir plus sur la requête (données qui passent pas directement par l'API)
# Fonctionnalité headers
print(response.headers)

# Résultat application/json
#jsondata = vrai info alors que response.headers donne