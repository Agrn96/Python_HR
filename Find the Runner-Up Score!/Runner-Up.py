# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Find the Runner-Up Score!
# 201612174

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
a = -101
b = -101
for i in arr:
    if(i>a): 
        b=a
        a=i
    elif(i>b and i<a): b = i
print(b)