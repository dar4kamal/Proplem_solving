numberOfEvents = int(input())

readyPolice = 0
unTreatedCrimeCount = 0

crimeStatus = [int(i) for i in input().split()]
"""
for crime in crimeStatus:
    unTreatedCrimeCount += crime
if unTreatedCrimeCount < 0:
    print(abs(unTreatedCrimeCount))
else:
    print(0)    

"""    
for crime in crimeStatus:
    readyPolice += crime
    
    if readyPolice < 0:
        unTreatedCrimeCount += abs(readyPolice)
        readyPolice = 0

print(unTreatedCrimeCount)
