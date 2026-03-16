marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):    # len : 리스트 안의 요소 개수를 리턴하는 함수 >> range(5)가 됨
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))