def bai(x):
    y = x*2
    return y
n = int(input())
for i in range(n+1):
    sample3 = list(map(int,list(str(i))))
sample1 = list(range(5))
sample2 = map(bai, sample1)
print(sample1)
print(list(sample2))
print(list(sample3))