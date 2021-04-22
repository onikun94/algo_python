M,H = map(int,input().split())
ans = H % M == 0
if ans:
    print("Yes")
else:
    print("No")