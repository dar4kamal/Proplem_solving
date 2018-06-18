
for i in range(1,6):
    row = input()
    rowList = row.split()
    rowList = [int(i) for i in rowList]
    if 1 in rowList:
        index = rowList.index(1)
        out = abs(3-(index+1)) + abs(3 - i)

print(out)