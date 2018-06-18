numberOfStones = int(input())

stoneRow = [stone for stone in input()]
originalStoneRow = stoneRow
stoneReference = stoneRow[0]
stoneIndex = 1

for i in range(numberOfStones-1):
    newStone = stoneRow[stoneIndex]
    if newStone == stoneReference:
        stoneRow[stoneIndex] = " "
    else:
        stoneReference = newStone
    stoneIndex += 1

stoneRow = [i for i in stoneRow if i != " "]    

print(len(originalStoneRow) - len(stoneRow))