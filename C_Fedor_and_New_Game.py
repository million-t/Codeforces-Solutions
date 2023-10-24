n, m, k = map(int, input().split())

armies = []
for _ in range(m + 1):
    armies.append(int(input()))


count = 0
fedor = armies[-1]
for i in range(m):
    if bin(fedor^armies[i]).count('1') <= k:
        count += 1

print(count)
