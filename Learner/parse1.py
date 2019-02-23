from bs4 import BeautifulSoup
import requests

res = requests.get('https://play.google.com/store/apps/details?id=com.uicashmagnet')
soup = BeautifulSoup(res.text, 'html.parser')
results = soup.findAll('span', attrs={'class': 'htlgb'})

print(results[1].text.strip())
