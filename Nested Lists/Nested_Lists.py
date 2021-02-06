# https://www.hackerrank.com/challenges/nested-list/problem
# Nested Lists
# 201612174
LScore = set()  # set removes duplicates
LName = []      # List to store the values of name and scores
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        LName.append([score, name])
        LScore.add(score)

sec_low = sorted(LScore)[1] # sorted set to get second lowest number
sec_low_name = []           # New List to store the names

for score, name in LName:   # List iteration to obtain names
    if score == sec_low:
        sec_low_name.append(name)

for i in sorted(sec_low_name): # Sorted names (Alphabetical)
    print(i, end='\n')
