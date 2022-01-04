a, b = map(int, input().split(' '))
n = 0
while a <= b:
    a = 3*a
    b = 2*b 
    n+=1
print(n)
    