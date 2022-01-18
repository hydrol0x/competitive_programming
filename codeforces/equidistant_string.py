output=[]
for i in range(int(input())):
    duplicates=[]
    nondup = []   
    string = str(input())
    flag=0
    for char in string:
        if (string.count(char) <= 1):
            flag+=1
            nondup.append(char)
        elif (2*char) not in duplicates:
            duplicates.append(2*char)

    output.append((''.join(duplicates))+(''.join(nondup)))
print(*output, sep="\n")