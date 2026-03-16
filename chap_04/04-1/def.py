# 일반적인 함수
# def 함수_이름(매개변수):
#     수행할_문장
#     ...
#     return 반환값

# EX
def add(a,b):
    result = a+b
    return result

a = add(3,5)
print(a)

# 입력값이 없는 함수
def say():
    return("Hi")
a = say()
print(a)

# 반환값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))
print(add(3,5))

# 매개변수 지정하여 호출
def sub(a,b):
    return a-b

result = sub(b=5, a=4)  # 순서 상관없이 사용 가능한 것이 장점
print(result)

# 여러 개의 입력값을 받는 함수 (입력값이 몇 개인지 모를 경우)
def add_many(*args):        # 매개변수 부분에 *를 붙인다
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# 매개변수로 하나만 사용할 수 있는 것은 아님
def add_mul (choice, *args):
    if choice == "add":         # 매개변수 choice에 add 입력 받았을 때
        result = 0
        for i in args:
            result += i
    elif choice == "mul":       # 매개변수 choice에 mul 입력 받았을 때
        result = 1
        for i in args:
            result *= i
    return result

result_add = add_mul("add", 1,2,3,4,5)
print(result_add)

result_mul = add_mul("mul", 1,2,3,4,5)
print(result_mul)

# 키워드 매개변수, kwargs
# 키워드 매개변수는 함수 호출 시 키워드=값 형태로 전달하는 매개변수를 받을 때 사용
# 매개변수 사용할 때는 매개변수 앞에 별 2개를 붙인다
def print_kwargs(**kwargs): 
    print(kwargs)

print_kwargs(a=1)   # 딕셔너리 형태로 출력. {'a': 1}

# 실용적인 예
def create_profile(**info):
    print("===프로필정보===")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이=30, 직업='프로그래머', 취미='독서')

# 일반 매개변수, 가변 매개변수, 키워드 매개변수 모두 사용 가능
def mixed_function(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수들: {kwargs}")

mixed_function("홍길동", 1,2,3, age=25, city="서울")


