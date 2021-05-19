# ######################### 모듈 ######################
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(3)
# theater_module.price_soldier(3)

# import theater_module as tm
# tm.price(3)
# tm.price_morning(3)
# tm.price_soldier(3)

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

# from theater_module import price, price_morning
# price(3)
# price_morning(3)
#price_soldier(3) #error

# from theater_module import price_soldier as price
# price(3)

################## 패키지 #######################
# import만 했을 땐 패키지, 모듈까지만 됨
# from : 모듈까지 import: 클래스, 함수까지 
# import travel.thiland ## 
# trip_to = travel.thiland.ThilandPackage()
# trip_to.detail()

# from travel.thiland import ThilandPackage
# ThilandPackage().detail()

# from travel import thiland
# trip_to = thiland.ThilandPackage()
# trip_to.detail()

############ __all__ ################
###############__name__###############
# from travel import *
# trip_to = thiland.ThilandPackage()
# trip_to.detail()
# trip_to_2 = vietnam.VietnamPackage()
# trip_to_2.detail()


# ################### 모듈 패키지 위치 ##############
# import inspect
# import random
# print(inspect.getfile(thiland))
# print(inspect.getfile(random))

##################### pip install #################
# from bs4 import BeautifulSoup
# # soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# # print(soup.prettify())
# # print(soup.find(text="bad"))
# # print(soup.i)
# # print(soup.p)
# soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", features="lxml")
# print(soup.prettify())
# print(soup.find(text="bad"))
# print(soup.tag1)
# print(soup.tag2)


############# 내장 함수 #################
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아해?")
# print("{0}은 아주 좋은 언어죠!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는 지표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle # 외장 함수
# print(dir())

# lst = [1, 2, 3]
# print(dir(lst))
# name = "kjiin"
# print(dir(name))


############ 외장함수 ##############
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td)

import byme
byme.sign()
