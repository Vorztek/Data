#Endpoint = http://api.github.com/users/username
#Passer en paramètres headers = contient dans un dictionnaire la clé token


import requests

# Stocker dans la variable headers la clé token dans un dictionnaire avec la clé authorization

#headers = {"authorization" : "token b6102f24b155e02ee81c4f9d97dbe2f09281055c"}
# Requête Get sur mon compte
# Passer le paramètre headers dans l'url
response = requests.get("https://api.github.com/users/DjangoPython66")

print(response.json())
