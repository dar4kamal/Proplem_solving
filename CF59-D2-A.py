word = input()

lowerCount = 0
upperCount = 0

for letter in [w for w in word]:
    if letter.lower() == letter:
        lowerCount += 1
    else:
        upperCount += 1

if lowerCount >= upperCount:
    print(word.lower())
else:
    print(word.upper())