numbers=[1,2,3,5,7,4,5,6,7,3,2,3,6,9,8,7,6,1,2,3,4,6,8,4,9,8,7,3.5]
counter={}

for number in numbers:
    if number in counter:
        counter[number]=counter[number]+1
    else:
        counter[number]=1

print(counter)
