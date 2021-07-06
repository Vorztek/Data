# On importe les elements
import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
from http import HTTPStatus

# On crée les deux premières listes

starts = [1, 51, 101]
years_url = list(range(2001, 2003))
# Ou starts = [str(i) for in in range(1,201,50)]
# years_url = [str(i) for i in range(2000,2018)]


title = []
year  = []
rate = []
metascore = []
data_value = []

for i in years_url:
    for y in starts:
        url = ("https://www.imdb.com/search/title/?title_type=tv_movie&release_date={}&sort=num_votes,desc&start={}&ref_=adv_nxt".format(i, y))
        #print(url)

        response = requests.get(url)
        #print(response)

        time.sleep(random.randint(1, 2)) # On rajoute le sleep

        # On import HTTPStatus depuis http. On transforme le résultat en liste qu'on met dans la variable code_status
        code_status = list(HTTPStatus)
        #print(code_status)
        # 200 égale le code_status[3]. Cela revient au même que chercher le résultat 200
        new_code = code_status[3]

        if new_code == HTTPStatus.OK:
            print("Tout fonctionne !")
        else:
            print("Aie..")

        # On met le contenu dans la variable content
        content = response.content
        # On utilise beautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        # Il faut qu'il affiche uniquement si le film a un meta score
        # On ne sait pas afficher les résultats uniquement pour chaque metascore

        if soup.select(".lister-item mode-advanced .ratings-metascore") is not None: # Ou inline-block ratings-metascore

                # On récupère tous les titres
                for z in soup.select("h3.lister-item-header >a"):
                    title = z.text
                    #print(title)

                # On récupère toutes les années
                for a in soup.find_all(class_ = "lister-item-year text-muted unbold"):
                    year = a
                    new_year = list(year)
                    #print(year.text)

                # On récupère toutes les notes
                for b in soup.find_all("strong"):
                    rate = b
                    #print(rate.text)

                # On récupère tous les metascore
                for c in soup.find_all(class_ = "inline-block ratings-metascore"):
                    metascore = c
                    #print(metascore.text)

                # for e in soup.find_all(class_ = "sort-num_votes-visible"):
                #     data_value = e
                #     new_data_value = data_value.text
                #     #print(new_data_value)

# Bon vu que ça fonctionne pas plus haut j'ai mis Panda pour la forme
df = pd.DataFrame({
          "title": title,
          "year": new_year,
          "rate": rate,
          "metascore": metascore,})
          #"data_value": new_data_value})

df




