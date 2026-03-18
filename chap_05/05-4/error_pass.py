# 오류를 완전히 무시하고 싶을 때 : pass

try:
    # 설정 파일을 읽으려 시도
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass    # 설정 파일이 없어도 계속 진행

print("프로그램이 정상적으로 실행됩니다.")