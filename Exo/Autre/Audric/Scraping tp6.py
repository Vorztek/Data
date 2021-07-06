# seven = soup.find("id= seven-day)
#
# forecast items = seven dayu .find all
#
# short_desc = today.find(class_ ="short_desc").txt
#
# forecast_tiems = seven_day.find_calmml(class_ ="tombstone-container")
# -
# temp = today.find(class="temp temp-high").text
# long_desc = today.find("img")
# long_desc_extract = long.desc["title"]
#
# print(long_desc_extract)
#
# # Isoler les tags de période pour pouvoir faire la boucle
#
# periods_tags = seven_day.select(".tombstone-container .period-name") # Deux elements, il faut rajouter un point
#
# # Conteneur global = "tombstone-container"
# # Conteneur de jour = "period_name
#
# # Boucle pour parcourir l'ensemble des élements de period_tags
# #Boucle sur l'ensemble des élement contenu dans le cadre
# # Comprehension de liste
#
# # Boucle sur du texte, à isoler avec .text
#
# periods = [pt.text() for pt in period_tags] #Nous allons extraire le texte de l'élement pt
# #La méthode text() renvoi une erreur, il faut utiliser get.text
# print(periods)
#
# short_desc = sd
# # Utiliser get_text sur l'élement
# # Boucle seven_days
# # Méthode .select
# # Passer l'arguement .tombstone-container & l'argument de la donnée visée
#
# temps = ts
# descs = ds

# ------------------
# Cours :

# Source
# https://forecast.weather.gov
# URL de départ: https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996
from bs4 import BeautifulSoup
import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996")
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)[:300] # Imprimer les premières lignes
# find = le premier élément qui correspond, find_all = toutes les correspondances
seven_day = soup.find(id="seven-day-forecast")
# print(seven_day)
# Quand vous utilisez l'élément "class" il faut rajouter un _ avant le =
forecast_items = seven_day.find_all(class_="tombstone-container")  # l'ensemble des conteneurs avec les jours
# print(forecast_items)
today = forecast_items[0]  # Prévision météo pour aujourd'hui
# print(today.prettify()) # Utiliser prettify pour afficher proprement le code source
# Periode/jour
period = today.find(class_="period-name").text  # Isolé la périodé
# print(period)
# Résultat attend = Today
# description courte
short_desc = today.find(class_="short-desc").text
# print(short_desc)
# Résultat attendu : Sunny
# Temperature
temp = today.find(class_="temp temp-high").text
# Description longue
long_desc = today.find("img")
long_desc_extract = long_desc["title"]
# print(long_desc_extract)
# Résultat attendu : Today: Sunny, with a high near 82.
# Light west southwest wind becoming west 6 to 11 mph in the afternoon.
# Isoler les tags de période pour pouvoir faire la boucle
period_tags = seven_day.select(
    ".tombstone-container .period-name")  # Deux élément, il faut rajouter un point au début de chacun
# print(period_tags)
# Conteneur global = "tombstone-container"
# Contenur de jour = "period-name"
# Boucle pour parcourir l'ensemble des élements de period_tags
# sur l'ensemble des élements contenu dans le cadre
# Compréhension de liste
# periods = [pt.text() for pt in period_tags] # Boucle sur du texte, à isoler avec .text
periods = [pt.get_text() for pt in period_tags]  # Nous allons extraire le texte de l'élement pt
print(periods)
# La méthode text() renvoi une erreur, il faut utiliser get_text()
# print(periods)
# 1. short_desc = sd
# Utiliser get_text sur l'élément
# Boucle seven_days
# Méthode .select
# Passer l'argument .tombstone-container & l'argument de la donnée visée
# 2. temps = ts
# 3. descs =  ds
# print(periods)
# Get_text ne marche pas
# voir img/title il s'agit d'une dicitonnaire utiliser = []
# import pandas as pd
#
# df = pd.DataFrame({
#     # les données " " = nommer les titres de colonnes
#     "periods": periods,
#     "short_desc":
#         "temp"
#         "desc"
# }
# )
# # df = nom du tableur
# pd.Dataframe # Appeler le tableur







