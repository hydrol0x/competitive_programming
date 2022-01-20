from math import ceil
distance = int(input())
# steps=0
# while distance > 0:
#     if distance >= 5:
#         steps+=1
#         distance-=5
#     elif distance == 4:
#         steps+=1
#         distance-=4
#     elif distance == 3:
#         steps+=1
#         distance-=3
#     elif distance == 2:
#         steps+=1
#         distance-=2
#     elif distance == 1:
#         steps+=1
#         distance-=1
# print(steps)

# optimum solution:

print(ceil(distance/5))
# because we take as many whole number steps of 5 as possible and then round up because we need one more step of 4,3,2, or 1 (or 0 if multiple of 5)