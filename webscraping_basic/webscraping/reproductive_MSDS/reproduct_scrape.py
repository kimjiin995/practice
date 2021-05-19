from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def reproduct_scrape():
    url = "https://msds.kosha.or.kr/MSDSInfo/kcic/msdssearchAll.do"

    # headless, user-agent
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36")

    # browser 생성
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    # parser soup객체 생성
    soup = BeautifulSoup(browser.page_source, "lxml")

    # 카스번호 검색
    elem = browser.find_element_by_id("searchKeyword")
    elem.send_keys("71-43-2")
    elem.send_keys(Keys.ENTER)

    # 공단 검색 자료 클릭
    elem = browser.find_element_by_xpath("//*[@id='Container']/div[2]/div[5]/table/tbody/tr/td[2]/a")
    elem.click()

    # loading 기다리기
    try:
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "Title11")))
    except:
        print("로딩이 깁니다. 브라우저를 끕니다.")
        browser.quit()

    # 독성에 관한 정보 클릭
    elem = browser.find_element_by_id("Title11")
    elem.click()

    # 생식독성 data 가져오기
    elem = browser.find_element_by_xpath("//*[@id='Contents11']/ul/li[2]/dl/dd[13]")
    print(elem.text)

    time.sleep(3)

