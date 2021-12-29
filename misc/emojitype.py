outputs=[]
for i in range(int(input())):
    string = input()
    for char in string:
        if string.count(char) > 1:
            outputs.append("Nope")
            break
    if len(outputs)!=(i+1):
        outputs.append("Emote Away")

print(*outputs, sep="\n")