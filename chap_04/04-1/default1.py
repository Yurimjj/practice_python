# 매개변수에 초깃값 미리 설정하기
def day_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나의 나이는 %d살 입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

day_myself('박응용', 27)
day_myself('박응용', 27, True)
day_myself('박응선', 27, False)