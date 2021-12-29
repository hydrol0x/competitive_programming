output = []
for i in range(int(input())):
    word = str(input())
    if len(word)>10:
        output.append(word[0]+str(len(word)-2)+word[-1])
    else:
        output.append(word)
print('\n'.join(output))   