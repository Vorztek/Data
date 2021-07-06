
#On importe les modules

import pprint  # similaire prettyfier
import requests
from bs4 import BeautifulSoup
import time  # DDOS #Ajouter des temps de chargement

#On crée les listes vides et la liste pour chaque page

name = []
year = []
rate = []
lst = [1, 51, 101]

#On crée la boucle for qui va parcourir à l'aide de lst les pages de IMDB

for i in lst:
    url = "https://www.imdb.com/search/title/?title_type=tv_movie&release_date=2000-01-01,2000-12-30&sort=num_votes,desc&start="+str(i)+"&ref_=adv_nxt"
    get = requests.get(url)
    # print(url)
    time.sleep(2)
    html = get.content
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    new_name = []
    new_year = []
    new_rate = []

#On boucle sur soup, on va dans h3, on transforme i en liste et on let met dans name et year. Si on print l'element 3 ou 5 de la liste crée ça fonctionne !

    for i in soup.select("h3"):
        name = list(i)
        #print(name[3].text)

    for i in soup.select("h3"):
        year = list(i)
        #print(year[5].text)

    for i in soup.select("strong"):
        rate = list(i)
        new_rate.append(rate)
        #print(rate[0])

# On utilise Panda, ça fonctionne avec new_rate. On utilise le [2:] parce que sinon il y a des phrases qui apparaisse
# Ne fonctionne pas avec year ni name alors que le print ressort exactement ce qu'on veut !!

    import pandas as pd
    df = pd.DataFrame({
          "rate": new_rate[2:]})
        # "year": new_year})
        # "rate": rate[0]})

    print(df)

    # C'est un test et ça fonctionne pas : df = pd.DataFrame(list(zip(name, year, rate)), columns = ["name,", "year", "rate"])
