N = input()
lengdata = int(len(N))
if N(lengdata) == '0':
    Ndata = str[:lengdata]
else:
    Ndata = N
leng = int(len(N))
length = int(len(Ndata) /2)
count = 0
if length % 2 == 0:
    for i in range(length):
        if Ndata[i] == Ndata[leng - i - 1]:
            count += 1
else:   
    for i in range(length):
        if Ndata[i] == Ndata[leng - i - 1]:
            count += 1

if count == length:
    print("YES")
else:
    print("NO")