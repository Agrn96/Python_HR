# https://www.hackerrank.com/challenges/piling-up/problem
# Piling Up!
# 201612174

n = int(input())
cubes = []
status = []
for i in range(n):
    amount = int(input())
    cubes = list(map(int, input().split()))
    rcubes = cubes.copy()
    rcubes.reverse()
    bottom = 0
    if (cubes[0] >= rcubes[0]):
        bottom = cubes[0]
    else: 
        bottom = rcubes[0]

    for i in range(amount):
        if (cubes[0] >= rcubes[0] and cubes[0] <= bottom):
            bottom = cubes[0]
            cubes.remove(cubes[0])
        elif (rcubes[0] >= cubes[0] and rcubes[0] <= bottom):
            bottom = rcubes[0]
            rcubes.remove(rcubes[0])
        else:
            status.append("No")
            break
        if(i==amount-1):
            status.append("Yes")
    
    cubes.clear()
    rcubes.clear()

for _ in status:
    print(_, end="\n")
