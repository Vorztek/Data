
#Mélanger les notions
# nb fautes Chelsea et passe de Paris
# <td> 24 </td>
# <td> 545 </td>

from bs4 import BeautifulSoup
import requests
response = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/results.html")
content = response.content
parser = BeautifulSoup(content, "html.parser")

#nbr_f = parser.find_all("tr", id = "fautes")[0]
nbr_f = parser.select("#fautes")[0]
chelsea_f = nbr_f.select("td")[1]

#Pour les passes

nbr_f = parser.select("#passes")[0]
paris_f = nbr_f.select("td")[2]

print(chelsea_f.text)
print(paris_f.text)

# Ou

print(nbr_f.text)


#Réponse Mellisa :
# response  = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/results.html")
# content = response.content
# parser = BeautifulSoup(content,"html.parser")
# nbr_f=parser.select("#fautes")[0]
# chelsea_f=nbr_f.select("td")[1]
# #nbr_f=parser.find_all("tr",id="fautes")[0]
# nbr_p=parser.select("#passes")[0].select("td")[2].text
# #paris_f=nbr_p.select("td")[2]
# print(chelsea_f.text)
# print(nbr_p)