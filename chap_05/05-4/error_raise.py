# 오류 일부러 발생시키기 : raise문 사용

class Bird:
    def fly(self):
        raise NotImplementedError   # 파이선 내장 오류, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류 발생 시키기 위해 사용
    

class Eagle(Bird):
    #오류 발생하지 않게하려면 다음 함수 구현해야함
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()