# for문의 응용
# 총 5명의 학생이 시험을 보았는데 점수가 60 이상이면 합격 그렇지 않으면 불합격
 
marks = [90, 25, 67, 45, 80]    # 학생들 시험 점수

number = 0                      # 학생에게 붙여줄 번호
for mark in marks:              # 90 25 67 45 80을 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)