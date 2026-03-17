class Fourcal:

    # 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):   # 메서드의 매개변수
        self.first = first              # 메서드의 수행문
        self.second = second            # 메서드의 수행문
        
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


a = Fourcal(4, 2)
b = Fourcal(3, 8)

# a.setdata(4, 2)
# b.setdata(3, 8)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

# 클래스의 상속
class MoreFourcla(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
    

a = MoreFourcla(4,2)
print(a.pow())
print(a.add())

# 메서드 오버라이딩 : 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
# FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성
class SafeFourCal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second

a = SafeFourCal(4,0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)