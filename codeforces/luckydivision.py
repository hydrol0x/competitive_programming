n = abs(int(input()))
answer=False
perfects = [4,7,44,77,47,74,444,777,474,747,447,744,774,477]
for perfect in perfects:
    if n%perfect==0:
        answer=True
if answer:
    print("YES")
else:
    print("NO")