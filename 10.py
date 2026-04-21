lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
nums = list(map(int, input().split()))
start = nums[0]
end = nums[1]
fragment = lst1[start:end + 1]
fragment.reverse()
lst2 = lst2 + fragment
del lst1[start:end + 1]
print(lst1)
print(lst2)
