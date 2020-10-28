# 소인수분해 프로그램
x=int(input("?"))
d=2                    # 2부터 나눕니다.


while d<=x:
    if x%d==0:          # x가 d로 나누어지면
        print(d)        # d는 약수이므로 출력
        x=x/d           # x를 d로 나눠서 다시 x에 저장합니다.
    else:
        d+=1            # 나누어지지 않으면 1을 더해서 반
