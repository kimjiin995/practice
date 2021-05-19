import requests
from bs4 import BeautifulSoup

url ="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 잘 갖고오는지 확인
# with open("송파헬리오시티.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows, 1):
    columns = row.find_all("td")
    deal = columns[0].get_text().strip()
    area = columns[1].get_text().strip()
    price = columns[2].get_text().strip()
    dong = columns[3].get_text().strip()
    floor = columns[4].get_text().strip()

    print(f'''\
================ 매물 {index} ===============
거래 : {deal}
면적 : {area}
가격 : {price}
동 : {dong}
층 : {floor}''')


