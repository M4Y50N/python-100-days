from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

best_movies = requests.get(URL)

soup = BeautifulSoup(best_movies.text, "lxml")


# print(soup.find(name=))
movies_100 = soup.select(".article-title-description__text h3")
movies_100.reverse()

for movie in movies_100:
    with open("movies.txt", mode="a", encoding="utf-8") as file:
        file.write(movie.text + "\n")




