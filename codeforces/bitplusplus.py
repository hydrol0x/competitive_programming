n = int(input())
total = 0
for i in range(n):
    program = input()
    for i in program:
        if i == '+':
            total+=0.5
        elif i == '-':
            total-=0.5
print(int(total))



# optimum solution, dont loop over entire str
# n=int(raw_input())
# x=0
# for i in range(n):
#     t=raw_input()
#     if(t[1]=='+'):
#         x+=1
#     else:
#         x-=1
# print x