import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.a) # 첫번째 a태그 불러옴
# print(soup.a.get_text())
# print(soup.a.attrs)
# print(soup.a["href"])

# Nbtn= soup.find("a", attrs={"class":"Nbtn_upload"}) # 처음 발견되는거 
# print(soup.find(attrs={"href":"/mypage/myActivity.nhn"}))
# print(Nbtn)
# print(Nbtn.get_text())
# print(Nbtn["href"])

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# # print(rank3.a.get_text())
# # print(rank1.find_next_siblings())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2)
# rank2 = rank3.find_previous_sibling()
# print(rank2)

webtoon = soup.find("a", text="참교육-26화")
print(webtoon)
