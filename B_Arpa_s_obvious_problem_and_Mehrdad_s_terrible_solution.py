from collections import defaultdict


n, x = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for num in a:
    dif = x^num
    ans += count[dif]
    count[num] += 1

print(ans)    
    