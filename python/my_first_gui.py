'''
CLI : Command Line Interface

GUI : Graphical User Interface
그래픽을 기반으로 사용자에게 제공되는 인터페이스

'''

import turtle 

player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.speed(9) # 1~10
screen = player.getscreen()

# 이 부분 작성에 따라 거북이 동작
'''
for i in range(30) :
    player.forward(60)
    player.right(90)
    player.forward(60)

for i in range(30) :
    player.backward(60)
    player.right(90)
    player.backward(60)
'''
#player.penup() # 그리기 x
#player.pendown() # 그리기
player.left(90)
player.forward(60)
player.right(180)
player.forward(60)
player.left(90)
player.forward(60)

player.left(90)
player.forward(60)
player.right(90)
player.forward(60)
player.right(90)
player.forward(60)
player.right(90)
player.forward(60)
player.right(180)
player.forward(90)

player.left(115)
player.forward(65)
player.backward(65)
player.right(65)
player.forward(65)
player.backward(65)

screen.listen() #focus on
screen.mainloop() # 유지