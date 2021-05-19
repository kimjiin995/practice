import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

f = open("1-200_시가총액.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,2):
    res = requests.get(url + str(page))

    soup = BeautifulSoup(res.text, "lxml")

    table = soup.find("table", attrs={"class":"type_2"})
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    for row in rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)
    
f.close()