# 오류 회피하기 : 특정 오류가 발생해도 그냥 통과시켜야 할 때가 있음 
            # ex. 여러 파일 처리 하는 중에 일부 파일 없더라도 프로그램 실행하고 싶을 때

students = ["김철수", "이영희", "박민수", "최유진"]

for student in students:
    try:
        with open(f"{student}_성적.txt", 'r') as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue    # 다음 학생으로 넘어감

# 위의 코드는 일부 학생의 성적 파일이 없어도 프로그램이 중단되지 않고 다른 학생들의 성적을 계속 처리할 수 있음.