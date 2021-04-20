n = int(input())
x, y = map(int, input().split())
a = sorted(map(int, input().split()), reverse = True)
t = list(map(int,input().split()))

for i in range(n):
    v, w = map(int, input().split())