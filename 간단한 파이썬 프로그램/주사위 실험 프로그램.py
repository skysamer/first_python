import random

total=1000000                 # 주사위 백만번 던지기
ev=0                          # 주사위를 던져서 2가 나온 횟수 저장
for i in range(total):
    if random.randint(1,6)==2:
        ev+=1

print(ev/total)
