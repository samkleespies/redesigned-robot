# python practice

import bs4 as bs
import urllib.request

# grab the sauce bois, and read it
sauce = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/baba/').read()

# pass the HTML code to BeautifulSoup
soup = bs.BeautifulSoup(sauce, 'lxml')

print("Current price of BABA: " + soup.td.string)
