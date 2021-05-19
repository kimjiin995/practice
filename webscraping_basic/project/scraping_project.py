import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

info_data = soup.find("div", attrs={"class":"info_data"})
cast_txt = info_data.find("p", attrs={"class":"cast_txt"}).get_text()
today_temp = info_data.find("span", attrs={"class":"todaytemp"}).get_text()
min_temp = info_data.find("span", attrs={"class":"min"}).get_text()
max_temp = info_data.find("span", attrs={"class":"max"}).get_text()
indicator = info_data.find("span", attrs={"class":"indicator"}).get_text()

dom = etree.HTML(str(soup))
fine_dust1 = dom.xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/dl/dd[1]/span[1]")
fine_dust2 = dom.xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/dl/dd[1]/text()")
# fine_dust2 = info_data.select("")
print("[오늘의 날씨]")
print(cast_txt)
print(f"현재 {today_temp}℃ (최저 {min_temp} / 최고 {max_temp})")
print(indicator)
print(f"미세먼지 {fine_dust1[0].text} {fine_dust2[0]}")