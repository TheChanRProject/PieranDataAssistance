from bs4 import BeautifulSoup
import requests

res = requests.get('https://play.google.com/store/apps/details?id=com.uicashmagnet')
soup = BeautifulSoup(res.text)
results = soup.findAll('span', attrs={'class': 'htlgb'})
for i in results:
    print(i)
