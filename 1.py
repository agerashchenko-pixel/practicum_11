digits = [int(input()) for numbers in range(10)]
num = [digits[i] + digits[i + 1] for i in range(9)]
print(num)
