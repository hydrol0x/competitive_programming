x_tot = 0
y_tot = 0
z_tot = 0
n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    x_tot += x
    y_tot += y
    z_tot += z
if abs(x_tot)+abs(y_tot)+abs(z_tot) != 0:
    print("NO")
else:
    print("YES")
