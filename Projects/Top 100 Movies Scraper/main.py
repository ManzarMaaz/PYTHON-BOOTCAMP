from typing import List
import requests
from bs4 import BeautifulSoup, Tag

URL: str = (
    "https://web.archive.org/web/20200518073855/"
    "https://www.empireonline.com/movies/features/best-movies-2/"
)

response: requests.Response = requests.get(URL)
soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

# Use a list comprehension for cleaner extraction
movie_names: List[str] = [
    tag.get_text(strip=True) 
    for tag in soup.find_all("h3", class_="title")
]

# Write in reverse order
with open("top100movies.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(reversed(movie_names)))
