########## 예외 처리 ################
# except ValueError, ZeroDivisionError, Exception(OUt of index)
# 계산기
# try:
#     num1 = int(input("숫자를 입력하시오"))
#     num2 = int(input("숫자를 입력하시오"))
#     num = []
#     num.append(num1/num2)
#     print(f"{num1} / {num2} = {num[1]}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as Error:
#     print(Error)
# except Exception as Error:
#     print(Error)
# except: 
#      print("알 수 없는 에러가 발생하였습니다.")

########### 에러 발생시키기 #############
# 한자리 숫자만 입력하는 계산기
# try:
#     num1 = int(input("한자리 숫자를 입력하시오 :"))
#     num2 = int(input("한자리 숫자를 입력하시오 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print(f"{num1} / {num2} = {num1/num2}")
# except ValueError:
#     print("한자리 숫자만 입력하시오")

############### 사용자 정의 에러 ##########33
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg


# try:
#     num1 = int(input("한자리 숫자를 입력하시오 :"))
#     num2 = int(input("한자리 숫자를 입력하시오 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1} / {num2} = {num1/num2}")
# except ValueError:
#     print("한자리 숫자만 입력하시오")
# except BigNumberError as err:
#     print("BigNumberError 입니다")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")


############ quiz ############
# 치킨 자동 주문 시스템
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1번부터 시작
while True:
    print(f"[남은 치킨 : {chicken}]")
    try:
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError 
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
                
    except ValueError as err:
        print("잘못된 값을 입력하였습니다. 1이상의 숫자를 입력하세요")
    except SoldOutError as err:
        print("SoldOutError")
        print(err)
        break
            
    

