class ThilandPackage:
    def detail(self):
        print("태국 관광 효도 50만원 판매중!")

if __name__ == "__main__":
    print("모듈을 직접실행했군요1")
    trip_to = ThilandPackage()
    trip_to.detail()
else:
    print("외부에서 모듈 호출!")