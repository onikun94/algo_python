n = int(input())
d = sorted(map(int,[input() for i in range(n)]))
#test = list(d)
ans = 1
for i in range(n-1):
    if d[i] < d[i+1]:
        ans += 1

print(ans)


