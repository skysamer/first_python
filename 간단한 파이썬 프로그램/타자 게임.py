import random
import time

w=["인생에서의 진정한 성공이란", "자주 그리고 많이 웃는 것.", "현명한 이에게서 존경을 받고", "아이들에게서 사랑을 받는 것."]

n=1            # 문제 번호
print("[타자 게임] 준비되면 엔터!")
input()                             # 사용자의 엔터를 기다림
start=time.time()

q=random.choice(w)
while n<=3:
    print("문제", n)
    print(q)
    x=input()
    if q==x:
        print("correct!")
        n+=1
        q=random.choice(w)
    else:
        print("wrong!")

end=time.time()
et=end-start
et=format(et, ".2f")
print("타자 시간: ", et, "초")
