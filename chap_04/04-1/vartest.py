# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a+1

vartest(a)
print(a)

# error
# def vartest(a):
#     a = a+1

# vartest(3)
# print(a)

# >>> vartest(3) 수행하면 함수 안에서 a는 4가 되지만 하무를 호출하고 난 후 print(a) 문장은 오류 발생
# >>> print(a)에서 사용한 a 변수는 어디에도 선언되지 않았기 때문


# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 01. return 사용하기 (추천)
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 02. global 사용하기 (추천하지 않음)
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)