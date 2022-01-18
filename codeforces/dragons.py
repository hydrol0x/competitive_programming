strength, n = map(int, input().split())
dragon = []
for i in range(n):
    dstrength,bonus = map(int, input().split())
    dragon.append((dstrength,bonus))

dragon.sort()


flag = 0 
for tuple in dragon:
    if tuple[0] < strength:
        flag+=1
        strength+=tuple[1]
    else:
        flag = 0
        break
if flag:
    print('YES')
else:
    print('NO')