import requests
from bs4 import BeautifulSoup
import time
import random
year_url = list(range(2001,2019))
start = [1, 51, 101, 151, 201]
titre = []
year = []
note_imdb= []
metascore = []
votes = []
for i in year_url:
    for y in start:
        url = ("https://www.imdb.com/search/title/?title_type=feature&release_date={}-01-01&start={}".format(i,y))
        response = requests.get(url)
        time.sleep(random.randint(8,15))
    #code_statuts = (200)
    #if i in code_statuts > 200():
        #print("il y a un message d'erreur")
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        for k in soup.select("h3.lister-item-header >a"):
            titre.append(k.text)
            print(titre)
