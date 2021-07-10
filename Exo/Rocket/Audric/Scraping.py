import requests
response = requests.get("https://raw.githubusercontent.com/Audrik1/HTML/master/1.html")
content = response.content
print(content)

