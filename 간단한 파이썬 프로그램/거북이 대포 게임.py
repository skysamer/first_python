import turtle as t
import random

def turn_up():
    t.lt(2)

def turn_down():
    t.rt(2)

def fire():                 # space bar를 누르면 거북이 대포 발사
    ang=t.heading()          # 현재 거북이가 바라보는 각도를 기억합니다.
    while t.ycor()>0:
        t.fd(15)
        t.rt(5)


    # while 반복문을 빠져나오면 거북이가 땅에 닿은 상태입니다.
    d=t.distance(target, 0)      # 거북이와 목표지점과의 거리구하기
    t.sety(random.randint(10,100))   # 성공 실패를 표시할 위치 정하기
    if d<10:                         # 목표지점과의 차이가 10미만이면 명중으로 처리
        t.color("blue")
        t.write("Good", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad", False, "center", ("", 15))

    t.color("black")
    t.goto(-200, 10)                # 거북이 위치를 처음으로 되돌림
    t.setheading(ang)              # 각도도 처음의 각도로 원위치


# 땅을 그립니다.
t.goto(-300, 0)
t.down()
t.goto(300, 0)

# 목표 지점을 설정하고 그립니다.
target=random.randint(50, 150)         # 목표 지점을 50~150사이의 임의의 수
t.pensize(3)
t.color("green")
t.up()
t.goto(target-10, 2)
t.down()
t.goto(target+10, 2)

# 거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌림

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# 거북이가 동작하는 데 필요한 설정을합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen()
    
    
