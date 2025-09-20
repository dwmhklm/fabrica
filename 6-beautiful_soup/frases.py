import bs4
import requests as r

url = 'https://quotes.toscrape.com/'
quotes = r.get(url)
status = quotes.status_code
soup = bs4.BeautifulSoup(quotes.text, 'html.parser')

frase = soup.find_all('div', class_='quote')

for div in frase:
    texto = div.find('span', class_='text').text
    with open("\\beautiful_soup\\frases.txt", 'a') as arquivo:
        arquivo.write(f'{texto} \n\n')