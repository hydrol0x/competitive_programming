answer = 0
chat = list(input())
word = ['h', 'e', 'l', 'l', 'o']
index=0
for c in chat:
    if index <= 4:
        if (c==(word[index])):
            answer+=1
            index+=1
if answer==5:
    print("YES")
else:
    print("NO")