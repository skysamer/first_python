import turtle as t
import random

score=0
playing=False         # 현재 게임이 플레이 중인지 확인하는 변수

te=t.Turtle()         # 악당 거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts=t.Turtle()         # 먹이
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

# 방향키 함수

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

# 게임을 시작하는 함수
def start():
    global playing
    if playing==False:
        playing=True
        t.clear()           # 메시지를 지우기
        play()

# 실행 함수

def play():
    global score
    global playing
    t.fd(10)
    if random.randint(1,5)==3:   #1~5사이에서 뽑은 숫자가 3이면(20%확률)
        ang=te.towards(t.pos())     # 어떤 각도로 가야되는지 알려줌
        te.setheading(ang)        # 악당이 주인공을 바라보게함
    speed=score+5

    if speed>15:
        speed=15
    te.fd(speed)
    if t.distance(te)<12:
        text="
                                # 게임 종료
                                


t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()
    
