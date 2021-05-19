import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items)
# print(items[0].find("div", attrs={"class":"name"}).get_text())
# item_name = soup.find("div", attrs={"class":"name"})
for item in items:
    # 광고 상품 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge"})
    if ad_badge:
        print("<광고상품은 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rating = item.find("em", attrs={"class":"rating"})
    if rating:
        rating = rating.get_text()
    else:
        rating="평점 없음"
        
    rating_count = item.find("span", attrs={"class":"rating-total-count"})
    if rating_count:
        rating_count = rating_count.get_text()
        rating_count = rating_count[1:-1]
    else:
        rating_count="평점 수 없음"
    
    # 평점 4.5 이상 & 평점수 100개 이상
    if float(rating) >= 4.5 and float(rating_count) >= 100:
        if "Apple" in name:
            print("<Apple 상품은 제외합니다>")
        else:
            print(f"상품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rating}")
            print(f"평점 수 : {rating_count}")
    