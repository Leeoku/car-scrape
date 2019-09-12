from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import os

url = input('Enter car link: ')
req = Request(url, headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'})
page = urlopen(req).read()
soup = BeautifulSoup(page,features = "lxml")

aPrice = soup.findAll("",{"class":"vehicle_price_result"})
if aPrice[0]:
    print (aPrice[0].text)

divs = soup.findAll('div', class_="pre_owned_left_div")
for div in divs:
    div.find()
print(divs)



'''
table = soup.find('div',{'class':"PreOwnedCarCategoryDetail"})
table_body = table.find('tr')


print(table_body)
rows = table_body.findAll('details-overview_data')

pricelist = []
for row in rows:
    pricelist.append(row)
print(pricelist)
'''
'''
for price in soup.findAll("",{"class":"vehicle_price"}):
    try:
        print (price.text)
        break
    except KeyError:
        pass
'''