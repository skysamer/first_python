import turtle as t

def polygon(n):
    for x in range(n):
        t.fd(50)
        t.lt(360/n)

def polygon2(n,a):
    for x in range(n):
        t.fd(a)
        t.lt(360/n)

polygon(3)
polygon(5)

# 그림을 그리지 않고 거북이를 100만큼 이동시킵니다.
t.up()
t.fd(100)
t.down()

polygon2(3, 75)
polygon2(5, 100)
