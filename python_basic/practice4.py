########## 함수 ############
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()


############ 전달값과 반환값 ##########
# def deposit(balance, money):
#     print(f"{money}원 입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print(f"{money}원 출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
#         return balance - money
#     else:
#         print(f"잔액이 부족하여 출금이 완료되지 못했습니다. 잔액은 {balance}원 입니다.")
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - commission - money # 튜플형태로 반환할수 있다.

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)

# commission, balance = withdraw_night(balance, 500)

# print(F"수수료는 {commission}원이며 잔액은 {balance}원 입니다.")


################## 기본값 ##################
# def profile(name, age=17, main_lang="python"):
#     print("이름은 {}, 나이는 {}, 주언어는 {}입니다"\
#         .format(name, age, main_lang))
    
# profile("유재석")


############ 키워드값 #############
# def profile(name, age=17, main_lang="python"):
#     print("이름은 {}, 나이는 {}, 주언어는 {}입니다"\
#         .format(name, age, main_lang))
    
# profile(name="유재석", main_lang="java", age="20")
# profile(main_lang="c", name="김태호", age = 20)


########## 가변 인자 ############
# def profile(name, age, *languages):
#     print(f"이름 : {name}\t 나이 : {age}\t언어 :", end=" ")
#     for lang in languages:
#         print(f"{lang}", end=" ")
#     print()

# profile("유재석", 25, "kotlin", "c", "c++")
# profile("김태호", 20, "java", 20)


########## 전역 변수 #################3
# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("함수 내 총의 갯수: {}".format(gun))

# print("전체 총의 갯수 : {}".format(gun))
# checkpoint(2)
# print("현재 총의 갯수 : {}".format(gun))

############ 지역 변수 ############# 매개변수와 리턴값을 써서
# gun = 10

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("함수 내 총의 갯수 : {}".format(gun))
#     return gun

# print("전체 총의 갯수 : {}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("현재 총의 갯수 : {}".format(gun))


################# quiz 표준체중 ################

# def std_weight(height, gender):
#     if gender == "남자":
#         std_weight = height * height * 22 * 0.0001
#     elif gender == "여자":
#         std_weight = height * height * 21 * 0.0001
    
#     return print(f"키 {height} {gender}의 표준 체중은 %0.2f입니다." % std_weight)

# std_weight(175, "남자")


# 영상 풀이

# def std_weight(height, gender):
#     if gender == "남자":
#         return round(height * height * 22, 2)
#     else: 
#         return round(height * height * 21, 2)

# height = 175
# gender = "남자"
# weight = std_weight(height/100, gender)

# print(f"키 {height} {gender}의 표준 체중은 {weight}kg입니다.")


######## 표준 입출력 ############
# sep, end
# print("python", "java", sep=" vs ", end= "? ")
# print("sure")

# # file
# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# # 시험 성적
# scores = {"수학":90, "영어":50}
# print(scores.items()) # 튜플의 리스트로 나옴
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(5), sep=":")

# #은행 대기순번표
# for num in range(1,31):
#     print(str(num).zfill(3))


# # 입력
# answer = input("아무값이나 입력하세요") #입력값 answer는 string으로 됨
# print(f"입력한 값은 {answer}입니다.")


########### 다양한 출력 포맷 ################
# print("{0: >10}".format(1000))
# print("{0:_>10}".format(1000))
# print("{0:_>+10}".format(1000))
# print("{0:_>+10}".format(-1000))
# print("{0:_>+10,}".format(-1000.88888))
# print("{0:_<+10,}".format(-1000))
# print("{0:_<+10}".format(1000))
# print("{0:,}".format(1000000))
# print("{0:+,}".format(1000000))
# print("{0:^<+30,}".format(1000000))


# #소수점출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))


############# 파일 입출력 ##################
# scores_file = open("scores.txt", "w", encoding="utf8")
# print("수학 : 90", file=scores_file)
# print("영어 : 99", file=scores_file)
# print("과학 : 98", file=scores_file)
# scores_file.close()

# scores_file = open("scores.txt", "a", encoding="utf8")
# scores_file.write("국사 : 97")
# scores_file.write("\n코딩 : 100")
# scores_file.close()

# scores_file = open("scores.txt", "r", encoding="utf8")
# print(scores_file.read())
# scores_file.close()

# scores_file = open("scores.txt", "r", encoding="utf8")
# print(scores_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(scores_file.readline(), end="")
# print(scores_file.readline(), end="")
# scores_file.close()

# scores_file = open("scores.txt", "r", encoding="utf8")
# while True:
#     line = scores_file.readline()
#     if not line:
#         break
#     print(line, end="")

# scores_file.close()

# scores_file = open("scores.txt", "r", encoding="utf8")

# for line in scores_file.readlines(): # list형태로 저장
#     print(line, end="")

# scores_file.close()


########## pickle ############## 프로그램상에서 사용하고 있는 데이터를 파일 형태로 저장

# import pickle

# pickle_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":"35", "취미":["농구", "수영", "자전거"]}
# pickle.dump(profile, pickle_file)
# pickle_file.close()

# pickle_file = open("profile.pickle", "rb")
# profile_r = pickle.load(pickle_file)
# print(profile_r)

# pickle_file.close()


############ with ################
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     #print("공부 열심히하고 있어요~", file=study_file)
#     study_file.write("공부 중!!")

# with open("study.txt", "r", encoding="utf8") as study_file_r:
#     print(study_file_r.read())


################### quiz ################## 350주차까지 보고서 만들기
# for num in range(1,51):
#     with open(f"{num}주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(f'''\
# - {num} 주차 주간보고 -
# 부서 : 
# 이름 :
# 업무 요약 :''')

# 영상 풀이
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(i))
        report_file.write("부서 :\n")
        report_file.write("이름 :\n")
        report_file.write("업무 요약 :")
