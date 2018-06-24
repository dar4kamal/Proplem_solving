
stripCalories = [int(i) for i in input().split()]
blackSqrSeq = [int(i) for i in input()]

sumOfCalories = 0
for i in blackSqrSeq:
    sumOfCalories += stripCalories[i-1]

print(sumOfCalories)