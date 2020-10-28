import turtle as t

angle=100          # 거북이가 왼쪽으로 회전할 각도를 지정(값 변경가능)
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(1,200):
    t.fd(x)
    t.lt(angle)
