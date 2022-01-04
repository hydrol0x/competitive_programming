string = str(input()).lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for c in vowels:
    string = string.replace(c, '') 
string = string.replace("", ".")
print(string[:-1])
