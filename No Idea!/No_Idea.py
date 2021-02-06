# https://www.hackerrank.com/challenges/no-idea/problem
# No Idea!
# 201612174

happiness = 0
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

arr = list(map(int, input().split()))
like = set(map(int, input().split()))
hate = set(map(int, input().split()))

for i in arr:
    if i in like:
        happiness+=1
    if i in hate:
        happiness-=1

print(happiness)
