numberOfSteps = int(input())

magnetReference = input()
magnetRow = magnetReference

for i in range(numberOfSteps-1):
    newMagnet = input()
    if newMagnet == magnetReference:
        magnetRow += newMagnet
    else:
        magnetReference = newMagnet
        magnetRow += " " + newMagnet

print(len(magnetRow.split()))