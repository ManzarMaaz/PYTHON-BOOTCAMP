import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

movie_name = soup.find_all('h3', class_='title')

movies_names = []

for name in movie_name:
    movies_names.append(name.get_text())

with open('top100movies.txt',mode='w') as file:
    for movie in movies_names[::-1]:
        file.write(f'{movie}\n')
