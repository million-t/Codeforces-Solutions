

n, m = list(map(int, input().split()))
prices = sorted(list(map(int, input().split())))

toyCount = {}
for _ in range(m):
    toy = input()
    toyCount[toy] = toyCount.get(toy, 0) + 1
count = sorted(toyCount.values())[::-1]
mn = 0
mx = 0
i = 0
for val in count:
    mn += val*prices[i]
    mx += val*prices[-1 -i]
    i += 1

print(mn, mx)
