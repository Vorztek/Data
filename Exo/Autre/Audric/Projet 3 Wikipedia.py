#Résultat attendu
# Titre = exemple = Life expectancy
# Desc = exempmle = "Human lifespan" redirects here. For the lifespan of a person in stages, see
# Titre de la table des matières = "Human patterns... Evolution and aging rate"
# Request
# Beautiful Soup
# Afficher le résultat des boucles avec les cités précédemment (titre, desc et table des matières)

from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/Life_expectancy")
soup = BeautifulSoup(page.content, 'html.parser')

titre = soup.find_all("h2")
for i in titre:
    print(i.text)

desc = soup.find(role = "note").text
#print(desc)

table_matieres = soup.find("ul").text
#print(table_matieres)