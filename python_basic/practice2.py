############### 리스트 #############
# index, count, append, insert, sort, reverse, clear, extend, 다양한 자료형
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬
# num_list = [1, 4, 5, 3, 2]
# print(num_list)

# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 가능
# mix_list = ["조세호", 20, "유재석", 40, True]
# print(mix_list)

# mix_list.extend(num_list)
# print(mix_list)

# print(mix_list[2])

############# 사전 #############
#[] : 불러오기(.get), 넣기, 대체하기    키 및 value 확인하기 : in , del 삭제, clear(), keys, values, items
# cabinet = {3:"유재석", 100:"김태호"}

# print(cabinet[3])
# print(cabinet.get(100))
# # print(cabinet[5]) # keyError
# # print(cabinet.get[5]) # none
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) #true
# print( 5 in cabinet) #False
# print( "유재석" in cabinet)

# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet.get("A-3"))
# print(cabinet["B-100"])

# cabinet["A-3"] = "김종국"
# print(cabinet)

# # list = ["유재석", "김태호"]
# # print(list)
# # list[0] = "김종국"
# # print(list)
# # list.replace("김종국", "하하") # list has no 'replace'
# # print(list)

# cabinet["C-3"] = "조세호"
# print(cabinet)

# # 삭제
# del cabinet["A-3"]
# print(cabinet)
# # del cabinet["조세호"] # keyError

# # list = ["사과", "바나나"]
# # del list[0]
# # print(list)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())


# cabinet.clear()
# print(cabinet)

#################### 튜플 #####################
# menu = ("돈까스", "생선까쓰")

# print(menu[0])

# #menu.append("치킨") # 튜플 추가안됨

# (name, age, hobby) = ("김종국", 20, "운동") # 변수 한번에 선언.
# print(name, age, hobby)

# profile = (name, age, hobby) = ("김종국", 20, "운동")
# print(profile)

# print(profile[0])

############### 집합(set) #################
# 중복안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["바나나", "딸기", "유재석"])

# print(java, python)

# # 교집합
# print( java & python)
# print(java.intersection(python))

# #합집합
# print(java | python)
# print(java.union(python))

# #차집합
# print(java - python)
# print(python.difference(java))

# python.add("김태호")
# print(python)
# java.remove("김태호")
# print(java)
# print(java.pop())
# print(java)


############## 자료구조의 변경 ##################
# hi_set = {"abc", 20, "bye"}
# print(hi_set, type(hi_set))
# hi_set = list(hi_set)
# print(hi_set, type(hi_set))
# hi_set = tuple(hi_set)
# print(hi_set, type(hi_set) )
# hi_set = set(hi_set)
# print(hi_set, type(hi_set) )


############ QUIZ #############
# from random import *
# id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# winner_ch = sample(id, 1)
# print(winner_ch)
# id.remove(winner_ch[0])
# winner_co = sample(id, 3)
# print(winner_co)
# shuffle(winner_co)
# result = f'''
#  -- 당첨자 발표 --
#  치킨 당첨자 : {winner_ch}
#  커피 당첨자 : {winner_co}
#   -- 축하합니다 --'''
# print(result)

#영상 풀이
from random import *
users = range(1, 21) # 1부터 20까지 생성
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) 
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 --")