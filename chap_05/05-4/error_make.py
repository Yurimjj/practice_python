# 예외 만들기 : 프로그램을 수행하다가 특수한 경우에만 예외처리를 하려고 종종 예외를 만들어 사용

class MyError(Exception):
    # 오류 메세지 구현
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

# say_nick("천사")
# say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

# 만약 오류 메세지를 사용하고 싶다면
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)