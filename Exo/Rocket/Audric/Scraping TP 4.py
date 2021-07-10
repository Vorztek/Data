import requests
from bs4 import BeautifulSoup
response  = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/4.html")
content = response.content
parser = BeautifulSoup(content, "html.parser")
# #Utiliser la fonction select
first_item = parser.select(".class2") # Quand on utilise la fonction select, il faut ajouter un point avant
print(first_item[0].text)  # C'est une liste

new_item = parser.select(".class1") # Quand on utilise la fonction select, il faut ajouter un point avant
print(new_item[1].text)

# TP 4

# Récup 2nd paragraphe classe 1
# 1er paragraphe class 2