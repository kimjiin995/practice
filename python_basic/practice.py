# print(5+3)
# print(2*8)
# print(3*(3+1))

# print('풍선')
# print("나비")
# print("ㅋ"*9)

# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 >10))
'''이렇게하면
    여러문장이
    주석처리 됩니다.'''

# animal = "고양이"
# name = "해피"
# age = 1
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " +  name + "예요")
# hobby = "공놀이"
# print(name,"는 ", age, "살이며, ", hobby + "을 아주 좋아해요")
# print( name + "는 어른일까요? " + str(is_adult))

# station = "인천공항"

# print(station + "행 열차가 들어오고 있습니다.")

# print(2**3) # 2^3
# print(10%3)
# print(10//3) #몫
# print( 5 <= 5)
# print( 3 == 3)

# print(1!=4)
# print(not(1!=4))

# print(1<3 and 3<5)
# print(1<3 & 3<5)

# print(1<3 or 1>3)
# print((1<3) | (1>3))
# print(1<2 | 3<1)

# print(1<5<7)

# print(2 + 3 * 4 ) #14
# print((2 + 3) * 4) #20
# number = (2 + 3) * 4
# print(number)
# number = number + 4 #24
# print(number)
# number += 3 #27
# print(number)
# number -= 2 # 25
# print(number)
# number /= 6 # 5
# print(number)
# number *= 6 # 30
# print(number)
# number %= 7 # 2
# print(number)
# number //= 1 # 2
# print(number)
# number **= 3 #8
# print(number)
# number =* 2 # 16
# print(number)

##############숫자 처리 함수################
# print(abs(-5)) #5
# print(pow(2, 3)) # 2^3 = 8
# print(max(4, 7)) # 7
# print(min(4, 7)) # 4
# num1 = 5 
# num2 = 8
# print(min(num1, num2)) # 5

# print(round(3.14)) #3 
# print(round(4.98)) #5

# from math import *
# print(floor(3.99)) #내림 3
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) #4

################## 랜덤 함수 #################

from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0 ~ 10 미만의 임의의 값 생성
# print (random() * 10 + 1 ) # 1 ~ 11 미만의 임의의 값 생성
# print(int(random() *10 ) + 1 ) # 1 ~ 10미만의 임의의 값 생성

# print(int(random() * 45) + 1 ) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성


# ################### 랜덤 날짜 ##############
# # 조건 : 28일 이내, 1~3일 제외
# study_date = randint(4, 28)
# print(study_date)
# study_date = int(random() * 25) + 4
# print(study_date)
# print("오프라인 스터디 모임 날짜는 매월 " + str(study_date) + "일로 선정되었습니다.")

# #################### 문자열 ###################
# sentence = "나는 여자입니다."
# print(sentence)
# sentence2 = '파이썬을 배우고 있습니다.'
# print(sentence2)
# print(sentence + sentence2)

# sentence3 = """
#             헬로우
#             나는 여자고
# 파이썬 배우는 중~~
# """
# print(sentence3)


############### 슬라이싱 ##################### 55:06
# jumin = "950824-2063319"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

################# 문자열 처리 함수 ##################
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("java")) #없으면 -1값.

# print(python.count("n"))

############## 문자열 포맷 #################
#방법 1.
# print("나는 %d살입니다" % 20)
# print("나의 이름은 %s입니다" % "김지인")
# print("나는 %d살이고 이름은 %s입니다" % (20, "김지인"))
# print("Apple은 %c로 시작합니다." % "A")
# print("나는 %s살입니다" % 20)

#방법 2
# print("나는 {}살입니다.".format(13))
# print("나는 {}살입니다.".format("13"))
# print("나는 {}살이고 이름은 {}입니다".format(13, "김지인"))
# print("나는 {1}살이고 이름은 {0}입니다".format(13, "김지인"))

#방법 3
# print ("나는 {age}살입니다".format(age=32))
# print ("나는 {age}살이고 이름은 {name}입니다.".format(age=22, name="tilla"))

#방법 4
# age = 21
# name = "kim jumin"
# print(f"나는 {age}살이고 이름은 {name}입니다")

# senten = f"나는 {age}살이고 이름은 {name}입니다"
# print(senten)


############## 탈출 문자 ################
# \n \" \' \\ \r \b \t
# print("안녕하세요
# \n김지인입니다.")
# print("안녕하세요 \"김지인\"입니다")
# print("c:\\Python39\\python_workspase")
# print("c:\Python39\python_workspase")
# print("Red Apple\rpine")
# print("Red Apple.\b, is so sweet")
# print("banana\tQueen")

########### 퀴즈 ##############
# 사이트별로 비밀번호를 만들어 주는 프로그램
# 규칙 1 : http:// 제외
# 규칙 2 : 처음만나는 . 이후 제외
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + ! 로 구성

# 내풀이
# url = "http://naver.com"
# point_index = url.index(".")
# remainder = url[7:point_index]
# password = remainder[:3] + str(len(remainder)) + str(remainder.count("e")) + "!"
# print(password)

#영상 풀이
# url = "http://daum.net"
# my_str = url.replace("http://", "") # 규칙 1
# my_str = my_str[:my_str.index(".")] # 규칙 2
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" 
# print(f"{url}의 비밀번호는 {password}입니다.")




