# import sys
# sys.stdin = open("whitesheet.in", 'r')
# sys.stdout = open("whitesheet.out", 'w')


x1, y1, x2, y2 = map(int, input().split()) # white sheet
x3, y3, x4, y4 = map(int, input().split()) # black one
x5, y5, x6, y6 = map(int, input().split()) # black two 


def interArea(x1, x2, y1, y2, x3, y3, x4, y4):
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = x1, y1, x2, y2
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = x3, y3, x4, y4
	
	return (min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y))


# ALg: If 

# if (interArea(x1, y1, x2, y2, x3, y3, x4, y4) + interArea(x1, y1, x2, y2, x5, y5, x6, y6)) == (y2-y1)*(x2-x1):
#     print("areas equal")
#     if (max(x4, x2)-x2) or (max(x6, x2)-x2) or abs((min(x1,x3)-x1)) or abs((min(x1,x5)-x1))\
#         or (max(x4, x2)-x2) or (max(x6, x2)-x2) or abs((min(x1,x3)-x1)) or abs((min(x1,x5)-x1)):
#         print("NO")
#     else:
#         print("YES")

# else:
#     print("NO2")