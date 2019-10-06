from selenium import webdriver
from bs4 import BeautifulSoup

url="http://en.vietnamexport.com/index.php/component/k2/itemlist/category/63-machine-and-equipment.html"
driver = webdriver.Chrome('/home/aiktc/Desktop/WEB SCRAPPING/day3/chromedriver')
driver.get(url)

html = driver.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(html, 'lxml')

div=soup.findAll('div',{'class': 'tintuc_item'})
text='/html/body/div[2]/div[1]/div/div[1]/div[3]/div[4]/ul/li[13]/strong'
file = open('assig.csv','w')
header = 'COMPANY NAME, EMAIL, TELEPHONE\n'
file.write(header)

for i in range(9):
    for element in div:
        name = element.h3.text
        name = name.split('\t\t')[1].split('\t')[0]

        email = element.a.text
        if(len(email)==0):
            email='NaN'

        telephone = str(element.div)
        telephone = telephone.split('Telephone')[1].split('<be/>')[0].split(':')[1]
        if(len(telephone)<8):
            telphone = 'NaN'

        #print(name + "/t" + email + "/t" + telephone)
        file.write(name.replace(',','|') + ',' + email.replace(',','|') + telephone.replace(',','|') + '/n')

    if(i!=8):
        find = driver.find_element_by_xpath(text)
        find.click()
        html = driver.execute_script('return document.documentElement.otherHtml')
        soup = BeautifulSoup(html, 'lxml')
        div = soup.findAll('div', {'class': 'tintuc_item'})

file.close()

