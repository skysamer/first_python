import math
import sys

print("ax2+bx+c=0")

# 계수 a,b,c를 입력받고, 입력받은 문자열을 소수로 바꿉니다.
a=float(input("a?"))
b=float(input("b?"))
c=float(input("c?"))

if a==0:
    print("이차방정식이 아닙니다.")
    sys.exit()         # 실행종료

d=b**2-4*a*c            # 판별식


if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print("2개의 해:", x1, x2)
if d==0:
    x=-b/(2*a)
    print("1개의 해:", x)
if d<0:
    print("해가 없습니다.")
