""" import pandas as pd
import requests
from bs4 import BeautifulSoup

country = []
cases = []
deaths = []
continent = []
name = []

url = ("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

for a in soup.find_all("tr"):
        name = list(a)
        continent.append(name[7].text)
        cases.append(name[3].text)
        deaths.append(name[5].text)
        country.append(name[1].text)

#         for i in soup.find_all('td')[0]:
#             country = i
#             print(country)
#         for i in soup.find_all('td')[1]:
#             cases = i
#             print(cases)
#         for i in soup.find_all('td')[2]:
#             deaths = i
#             print(deaths)
#         for i in soup.find_all('td')[3]:
#             continent = i
#             print(continent)

df = pd.DataFrame({
    "country": country,
    "cases": cases,
    "deaths": deaths,
    "continent": continent
})
df.to_csv("Covid2.csv")

# Resultat
# https://docs.google.com/spreadsheets/d/141_yBtLN6zIG3gLBBaESEo2hZ1osKKopbtQ3AwURxKo/edit?usp=sharing """