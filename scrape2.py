from requests_html import HTMLSession,HTMLResponse
import urllib.request

session = HTMLSession()
response = session.get("http://books.toscrape.com/")
#print(response)  #STATUS CODE OK(200)

source = response.html
#print(type(source))
#print(source)
#print(source.text)
#print(source.html)


# title=source.find('', first=True)
#print(title[0].text)

block = source.find('ol.row', first=True) #TAG 'OL' CLASS 'ROW'
#print(block) #ELEMENT
#print(block.text)  #ALL BLOCk

#title = block.find('li h3 a', first=True)
#print(title.text) #THE SHORT TITLE
#print(title.attrs['title']) #ATTRIBUTE OF TITLE IS 'title'
#print(title.attrs['href']) #LINK FOR THE TITLE


titles = block.find('li h3 a') #FOR ALL 
#for title in titles:
#    print(title.attrs['title'])
    #print(title.attrs['href']) 

#price = block.find('li p.price_color', first=True) #FOR FIRST
#print(price.text) #WITH EURO SIGN
#print(price.text[1:]) #WITHOUT EURO SIGN

prices = block.find('li p.price_color') #FOR ALL
# for price in prices:
#     print(price.text) #WITH EURO SIGN
    #print(price.text[1:]) #WITHOUT EURO SIGN

    #FOR APPENDING AND PRINTING
name = []
cost = []
for title in titles:
    name.append(title.attrs['title'])
for price in prices:
    cost.append(price.text)

#  for i in range(len(name)):
#     print(name[i])
#     print(cost[i])

#image = block.find('li div.image_container img', first=True)
#print('http://books.toscrape.com/'+image.attrs['src'])

images = block.find('li div.image_container img')

link = []

for image in images:
    link.append('http://books.toscrape.com/'+image.attrs['src'])




# divs = source.find('div.row', first=True)
# print(divs)

# for i in range(len(name)):
#     print(name[i])
#     print(cost[i])
#     print(link[i])
#     urllib.request.urlretrieve(link[i], name[i])
#     print('\n')

url=["http://books.toscrape.com/catalogue/page-2.html"]
for no in range(1,51):
    url.append(f"http://books.toscrape.com/catalogue/page-{no}.html")
    print(url)
