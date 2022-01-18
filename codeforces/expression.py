a = int(input())
b = int(input())
c = int(input())
# d
greatest = 0
if a+b+c > greatest:
    greatest = a+b+c
if a*b*c > greatest:
    greatest = a*b*c
if (a+b)*c > greatest:
    greatest = (a+b)*c
if (a*b) + c > greatest:
    greatest = (a*b) + c
if a+(b*c) > greatest:
    greatest = a+(b*c)
if a*(b+c) > greatest:
    greatest = a*(b+c)
print(greatest)
