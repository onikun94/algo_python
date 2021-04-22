A,B = map(int, input().split())
milkSolid = A+B
if 15<= milkSolid  and 8 <= B:
    print(1)
elif 10 <= milkSolid   and 3 <= B :
    print(2)
elif 3 <= milkSolid :
    print(3)
else:
    print(4)
    