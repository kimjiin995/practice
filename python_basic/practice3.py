############ if ################
# weather = input("오늘 날씨는 어떤가요?")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요없어요~")

# temp = int(input("오늘 기온은 몇도인가요?"))

# if 10 <= temp and temp < 40:
#     print("적당한 기온이군요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("두꺼운 외투를 챙기세요")

################ for ##################
# for wating_no in range(1,10,2):
#     print ("대기번호는 {}입니다".format(wating_no))

# wait_list = {"아이언맨", "토르", "원더우먼"}
# for customer in wait_list:
#     print(f"{customer}님 주문하신 음료나왔습니다.")


############## while #################
# customer = "토르"
# person = "unknown"
# index = 5
# while person != customer:
#     index -= 1
#     print(f"{customer}님 주문하신 음료 나왔습니다. 호출 {index}번 남았습니다.")
#     person = input("이름이 어떻게 되세요?")
#     if index == 0:
#         print("커피는 폐기처분되었습니다")
#         break
# index = 1
# while True:
#     print(f"{customer}님 주문하신 음료 나왔습니다. 호출 {index}번 했습니다.")
#     index += 1


########### continue, break ###############
# absent = [2, 5]
# no_book = [7]

# for student in range(1,31):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"책을 안가져온 사람이 있어서 수업진행은 더이상 못하겠구나. {student}번 교무실로 따라오렴")
#         break
#     print(f"{student}번 학생 책읽어보세요~")


############# 한줄 for ################## list의 값들을 한번에 바뀌는..
# list = list(range(11))
# print(list)
# 출석번호 100번부터 시작으로 바꾸기
# list = [i+100 for i in list]
# print(list)

# set = {i+100 for i in list}
# print(set)

# 학생이름을 길이로 변환
# student = ["아이언", "존", "사랑"]
# print(student)
# student = [len(i) for i in student]
# print(student)

# 학생이름을 대문자로 변환
# student = ["banana", "strawberry", "melon"]
# student = [s.upper() for s in student]
# print(student)


############ quiz ##################
# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# from random import *
# check = 0
# ox = "O or X"
# for index in range(1,51):
#     minute = randint(5,50)
#     if 5 <= minute <= 15:
#         ox = "O"
#         check += 1
#     else:
#         ox = " "
#     print(f"[{ox}] {index}번째 손님 (소요시간 : {minute}분)")

# print(f"총 탑승 승객 : {check}분")  

# 영상 풀이
from random import *
cnt = 0 # 총 탑승승객
for i in range(1, 51): # 1 ~ 50이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))
    

