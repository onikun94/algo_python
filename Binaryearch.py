n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))
ans =0

def binarySearch(x):
    left,right = -1, n
    def isMatch(i):
        return s[i] <= x
    while abs(left-right) >1:
        mid = (left+right)//2
        if isMatch(mid):
            left = mid
        else:
            right = mid
    return s[max(left,0)] == x

for data in t:
    if binarySearch(data):
        ans += 1
print(ans)
