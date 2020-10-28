numbers=[1,2,4,5,6,7,9,3,4,7,8,2,1,3,4,3,7,8,8,9]
counter={}

for number in numbers:
    if number in counter:
        counter[number]=counter[number]+1
    else:
        counter[number]=1

print(counter)
