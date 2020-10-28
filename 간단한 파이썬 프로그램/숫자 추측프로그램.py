import random as r

n=r.randint(1,30)

while True:         # 영원한 반복
    x=input("숫자를 맞혀보세요>>")
    g=int(x)
    if g==n:
        print("정답")
        break
    if g<n:
        print("너무 작아요")
    else:
        print("너무 커요")
    
