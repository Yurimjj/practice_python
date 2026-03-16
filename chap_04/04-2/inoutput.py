# 사용자 입출력

# input 사용하기 
# >> input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.
# >> input은 입력되는 모든 것을 문자열 취급
a = input()
print(a)

# 프롬포트를 띄워 사용자 입력받기
number = input("숫자를 입력하세요: ")
print(number)

# 입력값 정수로 변환
age = input("나이를 입력하세요: ")
age = int(age)
print(age + 1)

# 입력값 실수로 변환
height = input("키를 입력하세요(cm): ")
height = float(height)
print(height/100)   # 미터 단위로 변환

# 한 번에 변환하기
age = int(input("나이를 입력하세요: "))
print(type(age))    # age 타입 확인