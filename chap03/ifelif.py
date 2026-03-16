# 제어문

# if - else - elif 문
# 만약 3000원 이상의 돈을 가지고 있으면 택시, 그렇지 않으면 걸어가라
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라.")


# 전형적 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

