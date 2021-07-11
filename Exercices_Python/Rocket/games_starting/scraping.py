from bs4 import BeautifulSoup
from selenium import webdriver
import requests

year = []
#driver = webdriver.Chrome(executable_path=r'C:\Users\vion1\Downloads\chromedriver_win32\\chromedriver.exe')
#driver.get('https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on')



url = ("https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on")

response = requests.get(url)
print(response)
content = response.content
soup = BeautifulSoup(content, "lxml")

for link in soup.find_all(class_="flex-auto truncate"): #Ou draggableRecord rowCardContainer animate
    year = link.text
    print(year)

#driver.close()
