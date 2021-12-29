col_w_1 = 0
row_w_1 = 0
for i in range(5):
    row = input().replace(" ", "")
    if '1' in row:
        col_w_1 = row.index('1')
        row_w_1 = i
    else:
        pass
        # print(f'not in row {i}')
print(abs(3-col_w_1-1)+abs(3-row_w_1-1))

