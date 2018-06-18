numberOfCards = int(input())

SerejaScore = 0
DimaScore = 0

cards = [int(i) for i in input().split()]

for i in range(numberOfCards):
    if i%2 == 0:
        SerejaChoice = max(cards[0],cards[len(cards)-1])
        cards.pop(cards.index(SerejaChoice))
        SerejaScore += SerejaChoice
    else:
        DimaChoice = max(cards[0],cards[len(cards)-1])
        cards.pop(cards.index(DimaChoice))
        DimaScore += DimaChoice

print(SerejaScore,DimaScore)
