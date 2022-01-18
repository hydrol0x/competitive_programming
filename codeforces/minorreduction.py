# output=[]
# for i in range(int(input())):
#     integer = list(input())
#     integer = list(map(int, integer))
#     nums = []
#     for n, digit in enumerate(integer):
#         if integer[n] != integer[-1]:
#             integer2 = integer
#             integer2[n] = digit+integer[n+1]
#             integer2.pop(n+1)
#             nums.append(integer2)
#     output.append(max(nums))
# print(*output, sep="\n")

solutions = []
for i in range(int(input())):
    integer=input()
    

    outputs=[]
    if len(integer) <= 1:
        solutions.append(integer)
    else:
        integer = list(integer)
        integer = list(map(int, integer))
        for n, digit in enumerate(integer):
            integer2 = integer.copy()
            if integer[n] != integer[-1]:
                digit2 = integer[n+1]
                integer2[n] = digit+digit2
                integer2.pop(integer2.index(digit2))
                integer2 = ([str(digit) for digit in integer2])
                integer2 = ''.join(integer2)
                outputs.append(integer2)

        outputs = [int(integer) for integer in outputs]
        if outputs:
            solutions.append((max(outputs)))
print(*solutions, sep="\n")