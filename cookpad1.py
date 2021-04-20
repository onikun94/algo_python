x, y = map(str,input().split())

for num in range(len(y)):
    searchWord = y[len(y) - num :]
    if x.endswith(searchWord):
        saveWord = searchWord

print(saveWord)
