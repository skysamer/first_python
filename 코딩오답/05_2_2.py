min_a=2
max_a=10
total=100
memo={}

def pro(rest, sit):
    key=str([rest, sit])
    if key in memo:
        return memo[key]
    if rest<0:
        return 0
    if rest==0:
        return 1

    count=0
    for i in range(sit, max_a+1):
        count+=pro(rest-i, i)

    memo[key]=count
    return count


print(pro(total, min_a))
