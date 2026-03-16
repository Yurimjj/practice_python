# # 01 홀수, 짝수 판별하기
# # 주어진 자연수가 홀수? 짝수? 홀수면 True, 짝수면 False
def is_odd(number):
    if number%2 == 1:
        return True
    else:
        return False

is_odd(3)   # True
is_odd(4)   # False

# # 02 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

result1 = avg_numbers(1,2)
result2 = avg_numbers(1,2,3,4,5)
print(result1)
print(result2)

# # 03 프로그램 오류 수정하기 1
input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %d 입니다." %total)

# # 04 출력 결과가 다른 것은?
print("you""need""python")
print("you"+"need"+"python")
print("you", "need", "python")  # 콤마가 있는 경우 공백이 삽입되어 더해짐
print("".join(["you", "need", "python"]))

# 프로그램 오류 수정하기 2
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# 파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다
# 따라서 열린 파일 객체를 close로 닫아준 후 다시 열어서 파일 내용 읽어야 함

# 사용자 입력 저장하기
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()


# 파일의 문자열 바꾸기
# 파일을 모두 읽은 후에 문자열의 replace 함수를 사용하여 변경한 다음 저장
f = open('test.txt', 'r')
body = f.read()     # test.txt의 내용을 body 변수에 저장
f.close()

body = body.replace('java', 'pythone')  # body 문자열에서 변경

f = open("test.txt", 'w')   # 쓰기 모드로 열기
f.write(body)
f.close()


# 입력값을 모두 더해 출력하기
import sys
numbers = sys.argv[1:]  # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)

print(result)