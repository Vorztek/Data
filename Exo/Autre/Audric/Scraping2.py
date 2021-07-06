# import requests
#
# response = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/1.html")
# content = response.content
#
#
# #Parser = parcourir
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(content,"html.parser") # 1 Argument = le code html / 2 Argument parcourir le code
#
# # Isoler "un simple paragraphe"
# # Passer dans le body
# body = soup.body
#
#
# # Passer le p(paragraphe)
#
# paragraphe = body.p.text # le .text me permet de retirer les balises, le .p aller dans les balises <p>
# #print(paragraphe)
# # ------------------
# # TP 1 éléments
# # Consignes
# # Récupérer un exemple de page HTML grâce à la balise head
# # Récupérez le titre
# # Affichez le résultat
#
# head = soup.head
# title = head.title.text
# #print(title)
#
# #Utiliser la méthode FIND ALL
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(content,"html.parser")
# body = soup.find_all("body") #trouver les elements qui correspondent à ...
#
# paragraphe = body[0].find_all("p")
# print(paragraphe[0].text) # .Text impossible sur une liste, vous devez vous déplacer dans l'indice de position
#
# #------------
# # TP2
# # Consignes
# # Récupérer "Un exemple de page HTML" avec la méthode find_all
# # Utiliser les balises heads & title
#
# title = soup.find_all("title")
# #print(title[0].text)
#
# #Utiliser les IDs :
#
# # <!DOCTYPE html>
# # <html>
# #   <head>
# #       <title> Un exemple de page HTML </title>
# #   </head>
# #
# #   <body>
# #     <div>
# #       <p id="first">1er paragraphe</p>
# #     </div>
# #       <p id="second">2nd paragraphe</p>
# #   </body>
# # </html>
# #Récup first paragrpahe
# from bs4 import BeautifulSoup
# import requests







