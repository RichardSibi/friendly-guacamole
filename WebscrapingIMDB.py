from bs4 import BeautifulSoup
import requests
source = requests.get('http://www.imdb.com/search/title?release_date=" + year + “,” + year + “&title_type=feature')
soup = BeautifulSoup(source.content,'lxml')
i = 0
print("List of most popular movies for October 2021")
print()
for movie_sec in soup.find_all('div', class_ = 'lister-item-content'):
    heading = movie_sec.h3.a.text
    i += 1
    print('{}) Movie: {}'.format(i,heading))
    print()