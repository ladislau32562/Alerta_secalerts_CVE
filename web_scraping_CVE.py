# importar bibliotecas
from bs4 import BeautifulSoup
import requests


#criar variavel de url
url = "https://secalerts.co/cve-list"
# ver como funciona requição com user-agent
# headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

site = requests.get(url)

#variavel para guardar toda HTML
soupHTML = BeautifulSoup(site.content, "html.parser") # html.parser para analisar requição html
for tag in soupHTML.findAll('li', attrs={'class':'cve'}):
    CVEs = tag.find('a').contents[0]
    description = tag.find('p').get_text()
    with open('CVEs.csv', 'a', newline="",encoding='utf-8') as f:
        for cve in CVEs:
            CVEs = tag.find('a').contents[0]
            description = tag.find('p').get_text() + '\n'
            LINHA = CVEs + ";" + description
            f.write(LINHA)

    print(LINHA)
