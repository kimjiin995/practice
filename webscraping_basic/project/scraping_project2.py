import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

# 날씨
def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
   
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    curr_temp = soup.find("span", attrs={"class":"todaytemp"}).get_text()
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()
    light = soup.find("span", attrs={"class":"indicator"}).get_text().replace("8", "8 ")
    dust = soup.find("dl", attrs={"class":"indicator"}).find_all("dd")


    print("[오늘의 날씨]")
    print(cast)
    print(f"현재 {curr_temp}℃ (최저 {min_temp} / 최고 {max_temp})")
    print("오전 {} 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print(light)
    print(f"미세먼지 {dust[0].get_text()}")
    print(f"초미세먼지 {dust[1].get_text()}")
    print()

# 헤드라인 뉴스
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)

    news_lst = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_lst, 1):
        title = news.find("a").get_text().strip()
        link = news.find("a")["href"]
        print(f"{index}. {title}")
        print(f"(링크 : {url + link}")
    print()

# it 뉴스 가져오기
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    news_lst = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    
    for index, news in enumerate(news_lst, 1):
        a_idx = 0
        img = news.find("img")
        
        if img:
            a_idx = 1
       
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print(f"{index}. {title}")
        print(f"(링크 : {link})")
    print()

# 영어회화 가져오기
# def scrape_english():
#     print("[오늘의 영어 회화]")
#     url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
#     soup = create_soup(url)
#     
#     sub_lst_tag = soup.find_all("div", attrs={"class":"conv_txt"})
#     sub_lst_kor = sub_lst_tag[0].find_all("span", attrs={"class":"conv_sub"})
#     sub_lst_eng = sub_lst_tag[1].find_all("span", attrs={"class":"conv_sub"})
#     
#     print("(영어 지문)")
#     for sub in sub_lst_eng:
#         print(sub.get_text())

#     input("한글지문 보시려면 엔터를 입력하세요")
#     print("(한글 지문)")
#     for sub in sub_lst_kor:
#         print(sub.get_text())

# 정규식 이용해서 영어회화 가져오기
def scrape_english():
    print("[오늘의 영어 회화]")
    
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    
    print()
    
        

if __name__ == "__main__":
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()
    