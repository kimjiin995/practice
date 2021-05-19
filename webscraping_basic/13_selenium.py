from selenium import webdriver
import time
# pip install selenium
# 웹드라이버 설치, 크롬버전확인, chromedriver 다운
# browser.back(), forward(), refresh()
# from selenium.webdriver.common.keys import Keys
# elem.send_keys(Keys.ENTER)
# elem = browser.find_elements_by_id("")
# for e in elem:
#   e.get_attribute("href")

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

# 1. 로그인 화면 가기
browser.find_element_by_class_name("link_login").click()

# 2. 아이디, 비번 입력하기
browser.find_element_by_id("id").send_keys("id")
browser.find_element_by_id("pw").send_keys("password")

# 3. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 4. 아이디 지우고 다시입력
time.sleep(3)
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 5. html 정보 출력
print(browser.page_source)


browser.quit()

