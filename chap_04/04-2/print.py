# print 자세히 알기

# 큰 따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too" "short")
print("life" + "is" + "too" + "short")

# 문자열 띄어쓰기는 쉼표로 한다
print("life", "is", "too short")

# sep 매개변수로 구분자 설정하기
print("2025", "08", "16", sep="-")
print("점프", "투", "파이썬", sep=" TO ")

# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')