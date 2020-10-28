import turtle as t
n=5                # 오각형을 그립니다.
t.color("purple")
t.begin_fill()     # 색칠할 영역을 시작합니다.
for x in range(n):
    t.forward(50)
    t.lt(360/n)   # 거북이가 360/n만큼 회전 
t.end_fill()      # 색칠할 영역을 끝냅니다.
