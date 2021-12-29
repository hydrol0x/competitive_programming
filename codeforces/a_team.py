problems = 0
for i in range(int(input())):
    solvable = [int(j) for j in input().split()]
    if sum(solvable) >= 2:
        problems +=1
print(problems)