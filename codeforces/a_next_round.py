n, k = [int(i) for i in input().split()]
scores = [int(j) for j in input().split()]

output=0
for l in scores:
    if l>0 and l >= scores[k-1]:
        output += 1
    
print(output)