import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", {"class":"title"})
# # title = cartoons[0].a.get_text()
# # link = cartoons[0].a["href"]
# # print(title)
# # print("https://comic.naver.com"+link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)

# 평점 구하기
total_rates = 0
count = 0
cartoons = soup.find_all("div", {"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.strong.get_text()
    total_rates += float(rate)
    count += 1
total_rates = round(total_rates, 1)
print(total_rates, count)
print(len(cartoons))
print("평균 점수 : ", total_rates/count)



