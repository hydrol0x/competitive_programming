import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def interArea(x1, x2, y1, y2, x3, y3, x4, y4):
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = x1, y1, x2, y2
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = x3, y3, x4, y4
	
	return (min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y))

# if overlap on y direction and x direction, need to cover full area
# otherwise, cover just billboard area - intersect area
if (max(x4,x2)-x4)+abs((min(x1,x3)-x3)) and (max(y4,y2)-y4)+abs((min(y1,y3)-y3)) or \
    (max(x4,x2)-x4) and abs((min(x1,x3)-x3)) \
    or (max(y4,y2)-y4) and abs((min(y1,y3)-y3)):
    print((x2-x1)*(y2-y1))
else:
    print(((x2-x1)*(y2-y1)-(interArea(x1, x2, y1, y2, x3, y3, x4, y4))))