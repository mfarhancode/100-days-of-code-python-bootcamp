import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

web_html = response.text

soup = BeautifulSoup(web_html, 'html.parser')

all_movies = soup.find_all(name='h3', class_='title')

all_movies_list = []
for movie in all_movies:
    all_movies_list.insert(0, movie.getText())

movies_list_file = Path(__file__).parent.joinpath('movies_list.txt')

with open(movies_list_file, 'a', encoding="ISO-8859-1") as file:
    for m in all_movies_list:
        file.write(f'{m}\n')
    print('Movies list is saved in file:movies_list.txt')