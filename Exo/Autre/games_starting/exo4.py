from bs4 import BeautifulSoup
import urllib2
url = 'https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on'
data = urllib2.urlopen(url).read()

page = BeautifulSoup(data,'html.parser')

for link in page.findAll('a'):
       l = link.get('href')
       print(l)