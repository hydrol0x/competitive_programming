# sums = sorted(list(map(int, input().split("+"))))
# print(*sums, sep='+')

# greedy algorithm 
sums = list(map(int, input().split("+")))
sort_sums = []
for n, num in enumerate(sums):
    max = 0
    print(f"the current number is {num} at index {n}")
    if num >= max:
        print(f"the old max is {max}")
        max = num
        print(f"the new max is {max}")
    print(f"sorrted sums before append of {max} is {sort_sums}")
    sort_sums.append(max)
    print(f"sorted sums after append of {max} is {sort_sums}")
    print(f"sums before removal of {num}, sums: {sums}")
    sums.remove(num)
    print(f"sums after removal of {num}, sums: {sums}")
print(sums)
print(sort_sums)
