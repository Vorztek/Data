# import requests
# flux_logique_de_la_patate = requests.get("http://api.open-notify.org/iss-now.json")
# parameters = {"lat": 37.46, "long" : 122.28}
# flux_logique_de_la_patate = requests.get("http://api.open-notify.org/iss-now.json", params = parameters )
# content = flux_logique_de_la_patate.content
#
# print(content)

import json

#TP 2
# Consignes
# Convertir en chaine de caractères
# Reconvertir en dictionnaire
# Vérifier le type
sports_number= {
    "football":12349,
    "Tennis": 29282,
    "Equitation": 38383,
    "Basket": 83737
}

new_sport = json.dumps(sports_number)
print(type(new_sport))

new_new_sport = json.loads(new_sport)
print(type(new_new_sport))

#json.dumps pour transformer en str, .loads pour transformer en dictionnaire

#Obtenir un object
json.data = sports_number.json()
print(type(json.data))





