# 변수를 선언합니다.
i=0

# 무한 반복합니다.
while True:
    print("{}번째 반복문입니다.".format(i))
    i+=1
    input_text=input(">종료하시겠습니까?(y):")
    if input_text in["y"]:
        print("반복을 종료합니다.")
        break
