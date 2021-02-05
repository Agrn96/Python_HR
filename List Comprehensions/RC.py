# https://www.hackerrank.com/challenges/list-comprehensions/problem
# List Comprehensions
# 201612174

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k != n)]
print(list1);

# Primera Prueba sin List Comprehension
# list = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if(i+j+k != n):
#                list.append([i,j,k])