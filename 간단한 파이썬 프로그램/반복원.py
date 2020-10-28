import turtle as t

n=50                # 원을 50개
t.bgcolor("black")
t.color("green")
t.speed(0)           # 거북이 속도를 가장 빠르게 지정
for x in range(n):
    t.circle(80)
    t.left(360/n)
