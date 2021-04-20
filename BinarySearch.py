import bisect

n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))

ans = 0

for i in t:
    if bisect.bisect_right(s, i) - bisect.bisect_left(s,i) >0:
        ans += 1
print(ans)