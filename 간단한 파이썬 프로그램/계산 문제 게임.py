import random as r

def make_question():
    a=r.randint(1, 40)
    b=r.randint(1, 40)
    op=r.randint(1, 3)

    q=str(a)   # 여기에 문제를 만듦

    # 연산자 추가
    if op==1:
        q=q+"+"
    if op==2:
        q=q+"-"
    if op==3:
        q=q+"*"

    q=q+str(b)

    return q


# 정답/오답 횟수를 저장할 변수를 0으로 초기화합니다.
sc1=0
sc2=0

for x in range(5):       #5 문제
    q=make_question()
    print(q)
    ans=input("=")
    z=int(ans)

    if eval(q)==z:
        print("정답!")
        sc1+=1
    else:
        print("오답!")
        sc2+=1

print("정답:", sc1, "오답:", sc2)
if sc2==0:
    print("똥지리누;;")
        
