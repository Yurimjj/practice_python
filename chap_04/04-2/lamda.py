# lamda는 함수를 생성할 때 사용하는 예약어, def와 동일한 역할
# 함수르 한 줄로 간결하게 만들 때 사용, def를 사용할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 쓰임

# lamda
add = lambda a, b: a + b
result = add(3,4)
print(result)

# def
def add(a,b):
    return a+b
result = add(3,4)
print(result)
