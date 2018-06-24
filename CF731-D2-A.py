exhibitName = [i for i in input()]

letters = "abcdefghijklmnopqrstuvwxyz"
lettersDict = dict()
letterIndex = 1

for i in letters:
    lettersDict[i] = letterIndex
    letterIndex += 1

# print(lettersDict["a"])    

startIndex = "a"
rotationsCount = 0

for letter in exhibitName:
    currentIndex = lettersDict[startIndex]
    # print(currentIndex)
    if currentIndex <= 13 :
        currentIndex += 26
    else:
        currentIndex -= 26
    # print(lettersDict[startIndex] - lettersDict[letter])
    # print(currentIndex - lettersDict[letter])
    rotationsCount += min(abs(lettersDict[startIndex] - lettersDict[letter]), abs(currentIndex - lettersDict[letter]))
    startIndex = letter

print(rotationsCount)