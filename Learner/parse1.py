import bs4
import requests

res = requests.get('https://play.google.com/store/apps/details?id=com.uicashmagnet')
soup = bs4.BeautifulSoup(res.text)
rob = soup.find_all('<span class="htlgb">')

list1 = [i for i in rob]
print(list1)
