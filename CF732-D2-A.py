inp = input().split()
price = int(inp[0])
rCoin = int(inp[1])
pricesList = []

n = 1

while True:
    maxTotal = n * price - rCoin
    if maxTotal % 10 == 0 or n * price % 10 == 0:
        pricesList.append(maxTotal+rCoin)
        break
    n += 1

print(pricesList[0] // price)