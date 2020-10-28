import turtle as t
import random as r

t.shape("turtle")
t.speed(0)

for x in range(500):   # 거북이를 500번 움직임
    a=r.randint(1,180)
    t.setheading(a)    # 거북이 방향을 임의로 돌림
    b=r.randint(1,10)
    t.fd(b)
    
