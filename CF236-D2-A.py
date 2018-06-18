userName = input()

uniqueCharacters = set([letter for letter in userName])
# print(uniqueCharacters)

if len(uniqueCharacters)%2 != 0 :
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")