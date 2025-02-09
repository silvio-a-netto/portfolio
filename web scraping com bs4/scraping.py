import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://books.toscrape.com/'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('form', class_='form-horizontal').get_text().strip()
produtos = soup.find_all('article', class_=re.compile('product_pod'))

ultima_pagina = 50
#Dicionario com os dados coletados
dic_produtos = {'titulo':[], 'preco':[]}

#Loop entre as paginas
for i in range(1, ultima_pagina+1):
    url_pag = f"https://books.toscrape.com/catalogue/page-{i}.html"
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('article', class_=re.compile('product_pod'))
    #Loop entre os produtos para coleta dos dados
    for produto in produtos:
        titulo = produto.find("h3").find("a")["title"]
        preco = produto.find('p', class_=re.compile('price_color')).get_text().strip()

        dic_produtos['titulo'].append(titulo)
        dic_produtos['preco'].append(preco)

df = pd.DataFrame(dic_produtos)
df.to_csv('books_scraping.csv', encoding='utf-8', sep=';')
print("Scraping concluído! Dados salvos em 'books_scraping.csv'.")

