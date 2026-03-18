# 모듈 불러오기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

# 모듈 이름 없이 함수 이름만 쓰고 싶을 때
from mod1 import add
print(add(3, 4))

# 해당 모듈 함수 모두 쓰고싶을 때
from mod1 import add, sub
print(sub(4,2))
from mod1 import *
print(add(3, 4))
print(sub(4, 2))

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI, 4.4))