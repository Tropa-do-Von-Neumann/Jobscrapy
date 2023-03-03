import requests
from bs4 import BeautifulSoup
response = requests.get("https://br.linkedin.com/jobs/desenvolvedor-vagas?position=1&pageNum=0")


site = BeautifulSoup(response.text, 'html.parser')

noticias = site.find("section", attrs={"class": "two-pane-serp-page__results-list"})

titulo = site.find("ul", attrs={"class": "jobs-search__results-list"})

print(titulo.title)
