import random
print("# random 모듈")

print("- random():", random.random())
print("- uniform():", random.uniform(10,20))
print("- randrange():", random.randrange(20))

a = [1,2,3,4,5]

print("- choice():", random.choice(a))
print("- sample():", random.sample(a,2))
random.shuffle(a)
print("- shuffle():", a)


import random as ran

dice = ran.randrange(1,7)
guess = int(input("주사위 숫자 예상하기 :"))

if guess == dice :
    print("정답!")

else :
    print(" 실패!","\n","정답은 :", dice)

# 원하는 횟수만큼 로또번호 추첨
import random 


inte = int(input("정수 입력 : "))

for i in range(inte) :
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)
