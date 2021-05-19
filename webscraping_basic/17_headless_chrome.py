from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

# chrome headless
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # 소문자 x

# 페이지 이동
browser = webdriver.Chrome(options=options)
browser.get(url)
browser.maximize_window()

# 스크롤 내리기

# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 2080)")

# 페이지 맨아래로 스크롤
prev_height= browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break    
   
    prev_height = curr_height

print("스크롤 완료")

browser.get_screenshot_as_file("google_movie.png")

# parser에 넣기 (browser.page_source)
soup = BeautifulSoup(browser.page_source, "lxml")

# movie list 만들기
movies = soup.find_all("div", attrs={"class":"k6AFYd"})

# print(len(movies)) 

# movie마다 제목이랑 할인가격인것만 뽑기
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    prev_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    
    if prev_price:
        prev_price = prev_price.get_text() # NoneType 피하기
    else:
        continue
    
    curr_price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = "https://play.google.com" + movie.find("a")["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {prev_price}")
    print(f"할인 후 금액 : {curr_price}")
    print(f"링크 : {link}")
    print("-"*100)

# time.sleep(3)


