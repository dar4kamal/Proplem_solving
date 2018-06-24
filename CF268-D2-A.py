numberOfTeams = int(input())

homeUniforms = []
guestUniforms = []

for i in range(numberOfTeams):
    team = [int(j) for j in input().split()]
    homeUniforms.append(team[0])
    guestUniforms.append(team[1])

changeUniform = 0

for host in homeUniforms:
    for guest in guestUniforms:
        if host == guest:
            changeUniform += 1

print(changeUniform)    
