import requests
from bs4 import BeautifulSoup

source = "http://www.abmec.org.uk/memberslist/about-abmec-members/"
req = requests.get(source)
soup = BeautifulSoup(req.text,'lxml')

divs = soup.findAll('div', {'class':'row listmembers'})
links=[]
for div in divs:
    links.append(div.a.attrs['href'])

file=open('assi.csv','w')
header = 'COMPANY NAME, EMAIL, TELEPHONE, WEBSITE\n'
file.write(header)
for link in links:
    req=requests.get(link)
    soup = BeautifulSoup(req.text,'lxml')
    tel_p=soup.findAll('p',{'class':'tel'})
    email_p=soup.findAll('p',{'class':'email'})
    web_p=soup.findAll('p',{'class':'web'})
    tel=tel_p[0].text.replace('\xa0','').lstrip()
    email=email_p[0].a.attrs['href'].replace('mailto:','')
    web=web_p[0].a.attrs['href']
    name=soup.findAll('h2')[0].text
    print(name)
    file.write(name.replace(',','|')+','+email+','+tel+','+web+'\n')
file.close()    


