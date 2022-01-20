k, n, w = map(int, input().split())

sum = 0
for i in range(w+1):
    sum+=(k*i)
if sum-n <= 0:
    print(0)
else:
    print(sum-n)