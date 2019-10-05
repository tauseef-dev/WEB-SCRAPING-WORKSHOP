import requests
from bs4 import BeautifulSoup
import csv

csv_file = open("imdb.csv","w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['TITLE','TIME','GENRE','RATING','SUMMARY','DIRECTOR/S','STARS'])

source = requests.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs").text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

movies = soup.findAll(class_="nm-title-overview-widget-layout")
#print(type(movies))

for movie in movies:
            #FOR ALL MOVIES INFO
    # title = movie.find(class_="overview-top")
    # print(title.text)

            #for movies title
    # title = movie.h4
    # print(title)

            #for movie name only in text form
    title = movie.h4.text
    print(title)

        #for time
    try:
        time = movie.time.text
        print(time)
    
    except:
        time = "TIME NOT SPECIFIED"
        print('TIME NOT SPECIFIED')

    # genre = movie.p.findAll("span")
    # for genres in genre:
    #     print(genres.text)
            #FOR GENRE
    # genre = movie.span.text
    # print(genre)
        # FOR RIGHT WAY TO DISPLAY WITH GENRE
    genre = []
    
    for genres in movie.p.findAll("span"):
        genre.append(genres.text)
        print(genres.text)
    

        #FOR RATINGS
    try:
        rating = movie.find(class_="rating_txt").span
        print(rating.text)
    except:
        rating = "NO RATINGS AVAILABLE"
        print('NO RATINGS AVAILABLE')

    des = movie.find(class_="outline").text
    print(des)

    
    x=[]
    cast = movie.findAll("div",class_="txt-block")
    for ele in cast:
        x.append(ele.text)
    
        
    dire=x[0]
    star=x[1]
        #print(ele.text)
        
    print(dire)
    print(star)

    csv_writer.writerow([title,time,genre,rating,des,dire,star])
    print('\n')    
csv_file.close()
