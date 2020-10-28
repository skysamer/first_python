numbers=list(range(1, 10+1))

print(list(filter(lambda x:x%2!=0, numbers)))
print()

print(list(filter(lambda x: 3<=x<7, numbers)))
print()

print(list(filter(lambda x:x**2<50, numbers)))
