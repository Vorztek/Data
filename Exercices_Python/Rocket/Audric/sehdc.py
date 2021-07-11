# TP 3
# Consignes
# URL : http://open-notify.org/Open-Notify-API/People-In-Space/
# Combien de personne se trouvent dans l'espace en ce moment ?
# Module requests
# Assigner votre requête get à la variable response
# Transformer les données en json
# Isoler la clé contenant le nombre de personnes
# Résultat attendu: 3

import json
import requests


response = requests.get("http://open-notify.org/Open-Notify-API/People-In-Space/")
print(response)
