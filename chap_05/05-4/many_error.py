# 여러 개의 오류 처리하기
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

    # 인덱싱 오류가 먼저 발생했으므로 ZeroDivisionError 오류는 발생하지 않는다

# 오류 메세지도 다음과 같이 확인할 수 있다
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

# 오류를 함께 처리할 수도 있다
try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

    # 두 개 이상의 오류를 동일하게 처리하려면 괄호 사용