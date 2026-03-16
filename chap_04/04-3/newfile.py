f = open("새파일.txt", 'w')     # 현재 폴더에 파일 생김 (w-쓰기, r-읽기, a-추가)
for i in range(1, 11):         # 경로 정하고 싶으면 open("C:/doit/새파일") 맥은 ~/doit/...
    data = "%d번째 줄입니다. \n" %i
    f.write(data)

f.close()