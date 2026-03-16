# 파일 읽기

# readline 함수 사용하기
f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# 모든 줄을 출력하고 싶다면,
f = open("새파일.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()

# readlines 함수 사용하기 : readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트로 반환
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    # line = line.strip()    << 줄바꿈 문자 제거
    print(line)

f.close()


# read 함수 사용하기
f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()

# 파일 객체를 for 문과 함께 사용하기
f = open("새파일.txt", "r")
for line in f:
    print(line)

f.close()
