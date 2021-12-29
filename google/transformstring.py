# output =[]
# for t in range(int(input())):
#     s = str(input())
#     f = str(input())
#     ops = 0
#     for c in s:
#         direct_distance = abs(int(ord(f))-int(ord(c)))
#         indirect_distance = abs((26-direct_distance))

#         if direct_distance > indirect_distance:
#             ops+=indirect_distance
#         elif direct_distance < indirect_distance:
#             ops+=direct_distance
#     output.append(ops)
# for o in range(len(output)):
#     print("Case #{}: {}".format(o+1, output[o]))
output=[]
for t in range(int(input())):
    s = str(input())
    f = str(input())
    ops = 0
    for c in s:
        direct_distance = abs(int(ord(f))-int(ord(c)))

        ops+=min((direct_distance, abs(26-direct_distance)))
    output.append(ops)
for o in range(len(output)):
    print("Case #{}: {}".format(o+1, output[o]))