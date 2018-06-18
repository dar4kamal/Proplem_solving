
firstLine = input().lower()
secondLine = input().lower()

out = 0
if firstLine < secondLine:
    out = -1
elif firstLine > secondLine:
    out = 1

"""
for i in range(len(firstLine)):
    if firstLine[i] < secondLine[i]:
        out = -1
    elif firstLine[i] > secondLine[i]:
        out = 1
"""
print(out)