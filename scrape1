from requests_html import HTML
with open('simple.html') as source_file:
    file_content = source_file.read()
    source=HTML(html=file_content)

    title = source.find('title')
    #print(title[0].text)

    heading = source.find('#site_title')
    #print(heading[0].text)

    divs = source.find('.article')
    #print(type(divs))
    #print(divs)

    #for div in range(0,5):
        #print(divs[div].text)

    #div = divs[0]
    #print(div.text)

    #link = div.find('a', first=True)
    #print(type(link))
    #print(link)
    #print(link.text)
    #print(link.attrs['href'])


    print(title[0].text)
    print('\n')
    for i in range(len(divs)):
        # print(divs[i].html)
        div = divs[i]
    #for t in div:    
        print(div.text)
        link = div.find('a', first=True)
        print(link.attrs['href'])
        print('\n')

    
