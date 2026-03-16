# 01 조건문의 참과 거짓
# 다음 코드의 결과값은 ?
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")   # <<<< 결과값
elif "need" in a: print("need")
else: print("none")

print("#"*50)

# 02 3의 배수의 합 구하기
# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자
result = 0
i = 1
while i <=1000:
    if i%3 == 0:
        result += i
    i += 1

print(result)

print("#"*50)


# 별 표시하기
i = 0
while True:
    i += 1
    if i>5: break
    print("*"*i)

print("#"*50)


# 1부터 100까지 출력하기
for i in range(1,101):
    print(i)

print("#"*50)

# 평균 점수 구하기
# A 학급에 총 10명의 학생, 중간고사 점수는 [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for 문 사용하여 학급 평균 점수 구하기

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total/10      # 10 말고 len(A)사용
print(average)

print("#"*50)

# 리스트 컴프리헨션 사용하기
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)