import requests
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')

response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page=response.text

soup=BeautifulSoup(web_page,"html.parser")

get_movies=soup.find_all(name="h3", class_="title")
movies=[mov.getText() for mov in get_movies]
movies_order=movies[::-1]
for movie in movies:
    print(movie)
with open("best_movies_of_all_time.txt", "w") as file:
    for movie in movies_order:
        file.write(f"{movie}\n")

# movie_rank=[mov.split(") ", 1)[0] for mov in movies]
# movie_rank2=[int(mov.split(": ", 1)[0]) for mov in movie_rank]
# movie_title=[mov.split(") ", 1) for mov in movies]
# titles=[mov.split(": ",1) for mov in movie_title]
# print(movie_rank2)
# print(movie_title)