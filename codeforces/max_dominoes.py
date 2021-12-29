m, n = [int(i) for i in input().split()]
area = m*n
dominoes=0
while area > 1:
    area = area - 2
    dominoes+=1
print(dominoes)

# optimum is int(n*m/2).. dont overthink