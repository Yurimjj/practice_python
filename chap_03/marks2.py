# for문과 continue문

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue        # 점수가 60 미만 학생의 경우에는 continue문 수행 -> print문 수행 않고 for문 처음으로 돌아감
    print("%d번 학생 축하합니다. 합격입니다." %number)