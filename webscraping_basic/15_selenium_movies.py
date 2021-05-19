import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
    #  ,"Accept-Language":"ko-KR,ko"
    }

res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
elem = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(elem))

# with open("google_movie.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

for e in elem:
    title = e.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)