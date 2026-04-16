n = int(input())
delit = []

for i in range(1, n + 1):
    if n % i == 0:
        delit.append(i)
print(delit)