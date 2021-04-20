n, a, b = map(int, input().split())
ans = 0
for i in range(n+1):
    c = sum(list(map(int, list(str(i)))))
    print(c)
    if a <= c <= b:
        ans += i
print(ans)

