#1. short_desc = sd
# Utiliser get_text sur l'élément
# Boucle seven_days
# Méthode .select
# Passer l'argument .tombstone-container & l'argument de la donnée visée
#2. temps = ts
#3. descs =  ds
#print(periods)
# Get_text ne marche pas
# voir img/title il s'agit d'une dicitonnaire utiliser = []

from bs4 import BeautifulSoup
import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
print(forecast_items)

