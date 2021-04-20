a = sorted(map(int, input().split()), reverse = True)
x = a[0]
y = a[1]

for i in range(2,len(a)):
    if x < y:
        x += a[i]
    else:
        y += a[i]
print(max(x,y))
    