
numProblems = int(input())

problemSolved = 0

for problem in range(numProblems):
    problemThinkOf = input()
    patya = int(problemThinkOf.split()[0])
    vasya = int(problemThinkOf.split()[1])
    tonia = int(problemThinkOf.split()[2])

    if patya+vasya+tonia >= 2:
        problemSolved += 1        

print(problemSolved)
