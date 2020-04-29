from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening up connection and grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# get all item containers
containers = page_soup.findAll("div", {"class": "item-container"})

# create and open file to write to
filename = "products.csv"
f = open(filename, "w")

# create csv headers
headers = "brand, product_title, shipping \n"
f.write(headers)

# loop through item containers and write brand, title, shipping to csv
for container in containers:
  divWithInfo = container.find("div", "item-info")

  brand = divWithInfo.img["title"]
  product_title = divWithInfo.find("a", "item-title").text
  shipping = divWithInfo.find("li", "price-ship").text.strip()

  f.write(brand + ',' + product_title.replace(",", "|") + ',' + shipping + "\n")

f.close()