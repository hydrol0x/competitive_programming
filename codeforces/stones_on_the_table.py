n = int(input())
colors = list(list(input()))

removals = 0
for n, color in enumerate(colors):
    if ((n+1)!=len(colors)) and (color == colors[n+1]):
        removals+=1
print(removals)