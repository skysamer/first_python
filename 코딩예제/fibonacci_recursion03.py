counter=0


def fibonacci(n):
    counter+=1
    # 피보나치 수를 구합니다.
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# 함수를 호출합니다.
fibonacci(10)
