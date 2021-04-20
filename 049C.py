s = input()
data = ["erase", "eraser","dream", "dreamer"]
count = 0
count1 = 0
while 1:
    for frag in data:
        count += 1
        print("count =",count)
        if s.endswith(frag):
            count1 += 1
            s = s[:-len(frag)]
            print(s)
            print("count1 =",count1)
            break
    else:
        print("NO")
        break
    if not s:
        print("YES")
        break