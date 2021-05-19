############ class ################ 함수와 변수의 집합. 틀
# 생성자 __init__, 멤버변수 외부에서 쓰고 추가할 수 있음.
# 스타크래프트 유닛 클래스 만들기 : 

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name} 유닛이 생성 되었습니다.")
#         print(f"체력 {self.hp}, 공격력 {self.damage}")

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린2", 50, 10)
# tank = Unit("탱크", 60, 80)
# #tank = Unit("탱크") # Error

# print(tank.name)
# tank.clocking = True
# if tank.clocking == True:
#     print(f"{tank.name}은 현재 클로킹 상태입니다.")


##################### 메소드 ###############
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
        
#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")    
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 현재 체력이 다 소진되었습니다. ")
    
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat2 = AttackUnit("파이어뱃", 50, 25)

# firebat1.attack("5시")
# firebat2.damaged(25)
# firebat2.damaged(25)

############### 상속 ##################
# #일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

#공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
    
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
        
#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")    
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 현재 체력이 다 소진되었습니다. ")


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(self.name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# valkyrie1 = FlyableAttackUnit("발키리", 100, 15, 30)
# valkyrie1.fly(valkyrie1.name, "1시")


############# 메소드 오버라이딩 ################# 
# speed 추가해서 unit에 있는 move함수 FlyableAttackUnit에서 오버라이딩 하기
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]")

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
        
#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")    
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 현재 체력이 다 소진되었습니다. ")


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(self.name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# vulture.move("1시")

# battlecruiser = FlyableAttackUnit("battlecrusier", 80, 15, 20)
# battlecruiser.move("2시")


############## pass #############
# 함수 완성안해도 그냥 넘어가서 완성된것처럼
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# building1 = BuildingUnit("빌딩1", 20, "7시")

# def game_start():
#     print("게임을 시작합니다.")

# def game_end():
#     pass

# game_start()
# game_end()


# ##################### super ###############
# # 상속받을때 __init__함수에 쓰임. 다중 상속에서는 첫번째 클래스만 먹힘. self 빼야함

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)

# building1 = BuildingUnit("빌딩1", 20, "7시")
# building1.move("5시")

############# 스타크래프트 게임 ################# 
#speed 추가해서 unit에 있는 move함수 FlyableAttackUnit에서 오버라이딩 하기
#일반 유닛
# from random import *
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
    
#     def move(self, location):
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")    
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 현재 체력이 다 소진되었습니다. ")

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
        
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정시간 동안 이동 및 공격 속도를 증가. 자기 체력 10 감소
#     def steampack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가. 모든 탱크에 적용가능
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다. ".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다. ".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(self.name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == False:
#             self.clocked == True
#             print(f"{self.name} : 클로킹 모드 설정합니다.")
            
#         else:
#             self.clocked = False
#             print(f"{self.name} : 클로킹 모드 해제합니다.")

    
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     print("Player : gg") # 
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 tlwkr
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# #레이스 1기 생성
# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.steampack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
    
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21))

# # 게임 종료
# game_over()



########### quiz ###################
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type,self.deal_type, self.price, self.completion_year)
    
class Officetel(House):
    def __init__(self, location, deal_type, price, completion_year):
        House.__init__(self, location, "오피스텔", deal_type, price, completion_year)

apart1 = House("강남", "아파트", "매매", "10억", "2010년")
officetel1 = Officetel("마포", "전세", "5억", "2007년")
villa1 = House("송파", "빌라", "월세", "500/50", "2000년")

maemul = []
maemul.append(apart1)
maemul.append(officetel1)
maemul.append(villa1)


# last = maemul.pop()
# maemul.append(last)
# num = maemul.index(last) + 1
num = len(maemul)

print(f"총 {num}대의 매물이 있습니다.")
for m in maemul:
    m.show_detail()
