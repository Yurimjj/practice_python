# 전형적 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# for문과 함께 자주 사용하는 range 함수
# a = range(10) >> a range(0,10) => 0부터 10 미만의 숫자를 포함 (0~9)

# 예시
add = 0
for i in range(1,11):
    add = add + i
    print(add)


# for문과 break 문
for i in range(10):
    if i == 5:
        break       # i가 5가 되면 break문 실행, for문에서 빠져나간다
    print(i)

# for-else 문
for i in range(5):
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# break문으로 for 문을 빠져나가면 else절 실행 X
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")


# enumerate 함수 활용 : 리스트의 순서와 값을 함께 구하고 싶을 때는 enumerate 함수 사용하면 편리
fruits = ['apple', 'banana', 'orange']
for i, fruits in enumerate(fruits):
    print(f"{i}: {fruits}")

    #enumerate는 0부터 시작하는 인덱스 번호 자동으로 생성, 시작 번호 변경하고 싶을때는 enumerate(fruits, 1) << 1부터 시작

# zip 함수로 여러 리스트 함께 순회하기
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 세 개 이상의 리스트도 순회 가능
names = ['홍길동', '김철수', '이영희']
korean = [85, 92, 78]
english = [90, 88, 95]
for name, ko, eng in zip(names, korean, english):
    print(f"{name}: 국어 {ko}점, 영어 {eng}점")
