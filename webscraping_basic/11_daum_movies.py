import requests
from bs4 import BeautifulSoup

# 년도별로 반복하기
for year in range(2015, 2020):
    # 웹페이지 가져오기
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()

    # parser에 넣기
    soup = BeautifulSoup(res.text, "lxml")
    
    # img 태그 가져오기
    images = soup.find_all("img", attrs={"class":"thumb_img"})

    # 이미지 5개 반복하기
    for i, image in enumerate(images):
        
        # 이미지 url 가져오기
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        # 이미지 가져오기 
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # 이미지 파일만들기
        with open(f"movie_{year}_{i}.jpg", "wb") as f:
            f.write(image_res.content)
        
        # 5위까지 
        if i >= 4:
            break