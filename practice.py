# python practice

import bs4 as bs
import urllib.request

# grab the sauce bois, and read it
sauce = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/baba/').read()

# pass the HTML code to BeautifulSoup
soup = bs.BeautifulSoup(sauce, 'lxml')

print("Current price of BABA: " + soup.td.string)

# grab the sauce bois, and read it
sauce2 = urllib.request.urlopen('http://www.investopedia.com/markets/stocks/momo/').read()

# pass the HTML code to BeautifulSoup
soup2 = bs.BeautifulSoup(sauce2, 'lxml')

print("Current price of MOMO: " + soup2.td.string)
