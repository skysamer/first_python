import random

total=1000000                  # 실험을 백만번함
ev=0                           # 뽑힌 점이 사분원 안에 있는 횟수

for i in range(total):
    x=random.random()       # 0~1 사이의 실수
    y=random.random()

    if x**2+y**2<=1.0:
        ev+=1


print((ev/total)*4)


