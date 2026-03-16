# with문과 함께 사용하기
# 파일을 열면 한상 닫아주어야하는데 이것을 자동으로 해주는 게  with

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")