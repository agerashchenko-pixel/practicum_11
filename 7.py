digits = list(map(int, input().split()))
even_sum = sum(x for x in digits if x % 2 == 0)
odd_sum = sum(x for x in digits if x % 2 != 0)
print(even_sum, odd_sum)
