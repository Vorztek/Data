import requests
from bs4 import BeautifulSoup
response = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/2.html")
content = response.content
parser = BeautifulSoup(content, "html.parser")


first_p = parser.find_all("p", id = "second" )[0]
print(first_p.text)



import requests
from bs4 import BeautifulSoup
response = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/2.html")
content = response.content
parser = BeautifulSoup(content, "html.parser")


first_p = parser.find_all("p", id = "second" )[0]
print(first_p.text)

 # TP 3 ID
 #  Consignes
 #  Isoler le second parapraphe
 #  Résultat attendu : 2nd paragraphe