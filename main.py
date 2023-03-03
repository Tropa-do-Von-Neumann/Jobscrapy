import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get("https://br.linkedin.com/jobs/desenvolvedor-vagas?position=1&pageNum=0")
soup = BeautifulSoup(response.text, "html.parser")

with open("linkedin.html", "w", encoding="utf-8") as file:
    file.write(response.text)

cards = soup.find("ul", attrs={"class": "jobs-search__results-list"})
vagas = []

for card in cards.find_all("li"):
    titulo = card.find("h3", attrs={"class": "base-search-card__title"}).text.strip()
    empresa = card.find("h4", attrs={"class": "base-search-card__subtitle"}).text.strip()
    tipo = card.find("span", attrs={"class": "job-search-card__location"}).text.strip()
    
    vagas.append({
        "titulo": titulo.encode("utf-8"),
        "empresa": empresa.encode("utf-8"),
        "tipo": tipo.encode("utf-8"),
    })

pprint(vagas)
# pprint(soup.get_text())


