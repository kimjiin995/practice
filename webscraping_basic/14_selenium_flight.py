from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://flight.naver.com/flights/"

browser = webdriver.Chrome()
browser.maximize_window() #
browser.get(url)

# 가는날 선택
elem = browser.find_element_by_link_text("가는날 선택")
elem.click()
browser.find_elements_by_link_text("2")[1].click() # 다음달
browser.find_elements_by_link_text("30")[0].click() # 다음달

# 제주 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 로딩 기다리기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)