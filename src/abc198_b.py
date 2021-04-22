N = input()

NN = N.rstrip("0")

RN = NN[::-1]
print("Yes") if RN == NN else print("No")
