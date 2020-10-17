import bs4
import requests


def getAmazonPrice(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    article = soup.select('.product_bought_price>b')
    return article[0].text.strip()


print(getAmazonPrice('http://www.africa-shops.cm/product/jZ9Q5yKV/Hp_15_Ra_-_15.6_-_Intel_Dual_Core_N3060_-_4Go_-_500Go_-_Noir_-_Garantie_6_Mois.html'))
