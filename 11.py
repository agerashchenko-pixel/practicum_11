lst1 = list(map(int, input().split()))
shift = input()
direction = shift[0]
steps = int(shift[1:]) % len(lst1)
if direction == "R":
    lst1 = lst1[-steps:] + lst1[:-steps]
else:
    lst1 = lst1[steps:] + lst1[:steps]
print(list(lst1))
