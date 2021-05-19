from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

url = "http://daum.net"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

search = browser.find_element_by_id("q")
search.send_keys("송파 헬리오시티")
search.send_keys(Keys.ENTER)

soup = BeautifulSoup(browser.page_source)
real_estate = soup.find("div", attrs={"class":"wrap_tbl tbl_trade"})
tbody = real_estate.find("tbody")
trs = tbody.find_all("tr")
for i, tr in enumerate(trs, 1):
    deal = tr.find("td", attrs={"class":"col1"}).get_text().strip()
    area = tr.find("td", attrs={"class":"col2"}).get_text().strip()
    price = tr.find("td", attrs={"class":"col3"}).get_text().strip()
    dong = tr.find("td", attrs={"class":"col4"}).get_text().strip()
    floor = tr.find("td", attrs={"class":"col5"}).get_text().strip()

    print(f"============= 매물 {i} =============")
    print(f"거래 : {deal}")
    print(f"면적 : {area} (공급/전용)")
    print(f"가격 : {price} (만원)")
    print(f"동 : {dong}")
    print(f"층 : {floor}")
